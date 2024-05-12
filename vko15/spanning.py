from itertools import combinations

class AllTrees:
    def __init__(self, n):
        self.nodes = n
        self.edges = []
        self.temp_edges: []
        self.traversed: set

    def add_edge(self, a, b):
        self.edges.append((a, b))

    def __connected(self, a, b):
        if (a, b) in self.traversed:
            return False
        self.traversed.add((a, b))

        if a == b:
            return True

        for edge in self.temp_edges:
            connects = False
            if edge[0] == a: 
                connects = self.__connected(edge[1], b)
            if edge[1] == a:
                connects = self.__connected(edge[0], b)
            if connects:
                return True

        return False
        

    def __spanning(self, edges):
        self.temp_edges = edges
        for n in range(1, self.nodes+1):
            for m in range(1, self.nodes+1):
                self.traversed = set()
                connected = self.__connected(n, m)
                if not connected:
                    return False

        return True


    def count(self):
        spans = 0
        for comb in combinations(self.edges, self.nodes-1):
            if self.__spanning(comb):
                spans += 1

        return spans

if __name__ == "__main__":
    a = AllTrees(3)
    a.add_edge(1, 2)
    print(a.count()) # 0
    a.add_edge(1, 3)
    print(a.count()) # 1
    a.add_edge(2, 3)
    print(a.count()) # 3
