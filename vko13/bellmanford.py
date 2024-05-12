from random import randint, shuffle
from time import time

class BellmanFord:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []

    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))

    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0

        num_rounds = len(self.nodes) - 1
        for _ in range(num_rounds):
            for edge in self.edges:
                node_a, node_b, weight = edge
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance

        return distances

if __name__ == "__main__":
    nodes = range(1, 5001)
    bellmanford = BellmanFord(nodes)
    for a in nodes:
        for b in nodes:
            if a >= b or b - a >= 10:
                continue
            bellmanford.add_edge(a, b, randint(1, 1000))

    shuffle(bellmanford.edges)

    start = time()
    print(f"Time started at {start}")
    ans = bellmanford.find_distances(1)
    end = time()
    print(f"Time stopped at {end}")
    timed = time() - start

    print()
    print(f"Path length: {ans}")
    print(f"Time length: {timed}")
