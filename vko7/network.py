class Network:
    def __init__(self, n):
        self.computers = list(range(1, n+1))
        self.links = dict()
        for computer in self.computers:
            self.links[computer] = []

    def add_link(self, a, b):
        if not (a in self.computers and b in self.computers):
            raise IndexError

        self.links[a].append(b)
        self.links[b].append(a)

    def best_route(self, a, b):
        self._links_used = dict()
        self._paths = []

        self.__best_route_helper(a, b, 0)

        shortest = 0
        if not self._paths:
            shortest = -1
        else:
            shortest = min(self._paths)

        del self._links_used
        del self._paths
        return shortest

    def __best_route_helper(self, a, b, i):
        for dest in self.links[a]:
            if dest == b:
                self._paths.append(i+1)
                continue

            if (a, dest) in self._links_used and i+1 > self._links_used[(a, dest)]:
               continue

            #print(f"raaawr ({a} -> {dest}), i={i+1}")
            self._links_used[(a, dest)] = i+1
            self.__best_route_helper(dest, b, i+1)


if __name__ == "__main__":
    w = Network(5)
    w.add_link(1, 2)
    w.add_link(2, 3)
    w.add_link(1, 3)
    w.add_link(4, 5)
    print(w.best_route(1, 5)) # -1
    w.add_link(3, 5)
    print(w.best_route(1, 5)) # 2

    print()
    w = Network(5)
    w.add_link(4,5)
    w.add_link(2,3)
    print(w.best_route(3,4)) # -1
    print(w.best_route(3,4)) # -1
    w.add_link(4,5)
    w.add_link(3,4)
    w.add_link(2,5)
    w.add_link(4,5)
    print(w.best_route(4,5)) # 1
    w.add_link(3,4)
