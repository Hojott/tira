class Cities:
    def __init__(self, n):
        self.cities = list(range(1, n+1))
        self.roads = dict()
        for city in self.cities:
            self.roads[city] = []

    def add_road(self, a, b):
        if not (a in self.cities and b in self.cities):
            raise IndexError

        self.roads[a].append(b)
        self.roads[b].append(a)


    def has_route(self, a, b):
        self._places_been = set()
        self.__has_route_helper(a, b)

        istrue = False
        if b in self._places_been:
            istrue = True

        del self._places_been
        return istrue

    def __has_route_helper(self, a, b):
        self._places_been.add(a)
        for dest in self.roads[a]:
            if dest in self._places_been:
                continue
            self.__has_route_helper(dest, b)    


if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1, 2)
    c.add_road(1, 3)
    c.add_road(4, 5)
    print(c.has_route(1, 5)) # False
    c.add_road(3, 4)
    print(c.has_route(1, 5)) # True

    c = Cities(5)
    print(c.has_route(3,4))
    print(c.has_route(4,5))
    print(c.has_route(4,5))
    print(c.has_route(1,5))
    print(c.has_route(1,4))
    c.add_road(4,5)
    print(c.has_route(3,4))
    print(c.has_route(2,3))
    c.add_road(4,5)
    c.add_road(1,2)
