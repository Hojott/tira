class MaximumFlow:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {}
        for i in self.nodes:
            for j in self.nodes:
                self.graph[(i, j)] = 0

    def add_edge(self, node_a, node_b, capacity):
        self.graph[(node_a, node_b)] += capacity

    def add_flow(self, node, sink, flow):
        if node in self.seen:
            return 0
        self.seen.add(node)
        if node == sink:
            return flow
        for next_node in self.nodes:
            if self.flow[(node, next_node)] > 0:
                new_flow = min(flow, self.flow[(node, next_node)])
                inc = self.add_flow(next_node, sink, new_flow)
                if inc > 0:
                    self.flow[(node, next_node)] -= inc
                    self.flow[(next_node, node)] += inc
                    return inc
        return 0

    def construct(self, source, sink):
        self.flow = self.graph.copy()
        total = 0
        while True:
            self.seen = set()
            add = self.add_flow(source, sink, float("inf"))
            if add == 0:
                break
            total += add
        return total


def count(r):
    size = len(r)*len(r[0])*2
    mf = MaximumFlow(range(0, size))

    lenr0 = len(r[0])
    for x, row in enumerate(r):
        for y, tile in enumerate(row):
            if tile == "#":
                continue
            mf.add_edge((x*lenr0 + y)*2, (x*lenr0 + y)*2 + 1, 1)
            if x < len(r) - 1:
                mf.add_edge((x*lenr0 + y)*2 + 1, ((x+1)*lenr0 + y)*2, 1)
            if y < len(r[0]) - 1:
                mf.add_edge((x*lenr0 + y)*2 + 1, (x*lenr0 + (y+1))*2, 1)

    return mf.construct(1, size-2)

if __name__ == "__main__":
    r = [".....",
         ".###.",
         "...#.",
         "##.#.",
         "....."]
    print(count(r)) # 2

    r = [".....",
         ".....",
         "..#.#",
         ".....",
         "..#.."]
    print(count(r)) # 1
