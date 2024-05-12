import heapq

def calculate(t):
    graph = {}
    for i, v in enumerate(t):
        graph[i] = []
        if i-v >= 0:
            graph[i].append((i-v, v))
        if i+v <= len(t)-1:
            graph[i].append((i+v, v))

    distances = {}
    for node in range(len(t)):
        distances[node] = float("inf")
    distances[0] = 0

    queue = []
    heapq.heappush(queue, (0, 0))

    visited = set()
    while queue:
        node_a = heapq.heappop(queue)[1]
        if node_a in visited:
            continue
        visited.add(node_a)

        for node_b, weight in graph[node_a]:
            new_distance = distances[node_a] + weight
            if new_distance < distances[node_b]:
                distances[node_b] = new_distance
                new_pair = (new_distance, node_b)
                heapq.heappush(queue, new_pair)

    if distances[len(t)-1] == float('inf'):
        distances[len(t)-1] = -1

    return distances[len(t)-1]



if __name__ == "__main__":
    print(calculate([1, 1, 1, 1])) # 3
    print(calculate([3, 2, 1])) # -1
    print(calculate([3, 5, 2, 2, 2, 3, 5])) # 10
    print(calculate([7, 5, 3, 1, 4, 2, 4, 6, 1])) # 32
