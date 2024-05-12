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
    if not x: return []
    edges = [(1, 100)]
    x_left = x

    i = 0
    while 1:
        i += 1

        edges.append((1, i))
        edges.append((i, 100))
        for j in range(1, i):
            edges.append((j, i))
        
        while 1:
            if x_left - 2**i < 0:
                edges.pop()
                x_left += 2**i-1
            else:
                break
        
        x_left -= 2**i


    edges.pop()
    return edges

    

if __name__ == "__main__":
    for i in [2, 5, 10, 100, 150, 200, 123456789]:
        c = CountPaths(range(1, 101))
        ans = create(i)
        for edge in ans:
            c.add_edge(edge[0], edge[1])
        
        print(c.count_paths(1, 100))
    
