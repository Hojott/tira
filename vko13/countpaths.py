class CountPaths:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in self.nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)

    def count_from(self, node):
        if node in self.result:
            return self.result[node]

        path_count = 0
        for next_node in self.graph[node]:
            path_count += self.count_from(next_node)

        self.result[node] = path_count
        return path_count

    def count_paths(self, x, y):
        self.result = {y: 1}
        return self.count_from(x)

if __name__ == "__main__":
    verkko = CountPaths(list(range(1, 101)))
    for i in range(2, 102):
        verkko.add_edge(1, i)
    for i in range(2, 101):
        verkko.add_edge(i, i+1)

    print(verkko.count_paths(1, 101))
