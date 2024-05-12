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
    knights = []
    matches = {}
    # Gather knights
    for x, row in enumerate(r):
        for y, square in enumerate(row):
            if square == ".":
                continue
            knights.append((x, y))
            matches[len(knights)-1] = []
    
    mf = MaximumFlow(range(1, len(knights)*2+4))

    # Find matches
    for k1, (kx, ky) in enumerate(knights):
        for i in range(8):
            nx, ny = [(-2, 1), (-2, -1), (2, 1), (2, -1), \
                      (1, -2), (1, 2), (-1, 2), (-1, -2)][i]

            if 0 > kx+nx or kx+nx >= len(r):
                continue
            if 0 > ky+ny or ky+ny >= len(r[0]):
                continue
            if r[kx+nx][ky+ny] == ".":
                continue

            k2 = knights.index((kx+nx, ky+ny))
            matches[k1].append(k2)
            mf.add_edge(k1+3, k2+len(knights)+4, 1)

    for i in range(3, len(knights)+3):
        mf.add_edge(1, i, 1)
        mf.add_edge(i+len(knights)+1, 2, 1)




    """
    s1 = set()
    s2 = set()
    undecided = set()
    # Sort into two groups
    while 1:
        undecided_cp = undecided.copy()
        for k1, _ in enumerate(knights):
            if k1 in s1 or k1 in s2:
                continue
            
            for k2 in matches[k1]:
                if k2 in s1:
                    s2.add(k1)
                    if k1 in s1:
                        # shouldnt do this?
                        print("aaaaah")
                    break
                if k2 in s2:
                    s1.add(k1)
                    if k1 in s2:
                        print("aaaah")
                    break

            if k1 in undecided:
                undecided.remove(k1)

            if k1 not in s1 and k1 not in s2:
                undecided.add(k1)

        if not undecided:
            break
        
        if undecided_cp == undecided:
            k = list(undecided)[0]
            s1.add(k)
            undecided.remove(k)

    for k in s1:
        mf.add_edge(1, k+3, 1)
    for k in s2:
        mf.add_edge(k+3, 2, 1)
    """

    #print(matches)
    #print(s1, s2)
    return mf.construct(1, 2)//2


if __name__ == "__main__":
    r = ["*.......",
         "..*...*.",
         "........",
         ".*......",
         "...*....",
         ".......*",
         "........",
         "......*."]
    print(count(r)) # 3

    r = ["***.*...",
         ".*...***",
         "**..*..*",
         "..*.*..*",
         ".*.....*",
         ".***.**.",
         "...*...*",
         "**..*.**"]
    print(count(r)) # 10
