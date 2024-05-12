class CountPaths: # For debugging
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


def create(x):
    points = []

    i = 1
    while x > 0:
        if x % 2:
            points.append(i*2)

        i += 1
        x //= 2

    edges = [(1, 2)]

    i = 0
    while i < points[-1]:
        i += 2
        edges.append((i,   i+2))
        edges.append((i,   i+1))
        edges.append((i+1, i+2))
        if i in points:
            edges.append((i, 100))

    return edges

    

if __name__ == "__main__":
    for i in [2, 5, 10, 100, 150, 200, 123456789]:
        c = CountPaths(range(1, 101))
        ans = create(i)
        for edge in ans:
            c.add_edge(edge[0], edge[1])
        
        print(c.count_paths(1, 100))
    
