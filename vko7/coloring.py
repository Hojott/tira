class Coloring:
    def __init__(self, n):
        self.web = dict()
        for i in range(1, n+1):
            self.web[i] = set()

        self._places_been: set
        self._original: int
        self._cancolor: bool

    def add_edge(self, a, b):
        self.web[a].add(b)
        self.web[b].add(a)

    def check(self):
        self._cancolor = True
        for node in self.web:
            self._places_been = set()
            self._original = node

            self.__check_helper(node, 0)
            cancolor = self._cancolor

            #del self._places_been
            #del self._original
            #del self._cancolor

            if not cancolor:
                break

        return cancolor
            
    def __check_helper(self, node, depth):
        self._places_been.add(node)
        if not self._cancolor:
            return

        if depth and node == self._original:
            if depth % 2:
                self._cancolor = False

        for next_node in self.web[node]:
            if next_node in self._places_been and next_node != self._original:
                continue
            self.__check_helper(next_node, depth+1)
        


if __name__ == "__main__":
    c = Coloring(4)
    c.add_edge(1, 2)
    c.add_edge(2, 3)
    c.add_edge(3, 4)
    c.add_edge(1, 4)
    print(c.check()) # True
    c.add_edge(2, 4)
    print(c.check()) # False
