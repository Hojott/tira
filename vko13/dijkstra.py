import heapq
from random import randint, shuffle
from time import time

class Dijkstra:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))

    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0

        queue = []
        heapq.heappush(queue, (0, start_node))

        visited = set()
        while queue:
            node_a = heapq.heappop(queue)[1]
            if node_a in visited:
                continue
            visited.add(node_a)

            for node_b, weight in self.graph[node_a]:
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    new_pair = (new_distance, node_b)
                    heapq.heappush(queue, new_pair)

        return distances

if __name__ == "__main__":
    nodes = range(1, 5001)
    dijkstra = Dijkstra(nodes)
    for a in nodes:
        for b in nodes:
            if a >= b or b - a >= 10:
                continue
            dijkstra.add_edge(a, b, randint(1, 1000))

    for node in dijkstra.graph:
        shuffle(dijkstra.graph[node])

    start = time()
    print(f"Time started at {start}")
    ans = dijkstra.find_distances(1)
    end = time()
    print(f"Time stopped at {end}")
    timed = time() - start

    print()
    print(f"Path length: {ans}")
    print(f"Time length: {timed}")
