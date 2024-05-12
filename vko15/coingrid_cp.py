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
    coins = []
    # Gather coins
    for x, row in enumerate(r):
        for y, square in enumerate(row):
            if square == ".":
                continue
            coins.append((x, y))
    
    mf = MaximumFlow(range(1, len(coins)*2+4))

    # Find matches
    for c1, (x1, y1) in enumerate(coins):
        for c2, (x2, y2) in enumerate(coins):
            if x1 == x2 and y1 == y2:
                continue
            if x1 == x2 or y1 == y2:
                mf.add_edge(c1+3, c2+len(coins)+4, 1)

    for i in range(3, len(coins)+3):
        mf.add_edge(1, i, 1)
        mf.add_edge(i+len(coins)+1, 2, 1)


    return mf.construct(1, 2)//2


if __name__ == "__main__":
    r =["........",
        "........",
        "...X..X.",
        "........",
        "....X...",
        "..X.X..X",
        "........",
        "....X..."]
    print(count(r)) # 3

    r =[".....",
        "...X.",
        ".....",
        "X....",
        "....."]
