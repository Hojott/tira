class UnionFind:
    def __init__(self):
        self.link = {}
        self.size = {}

    def find(self, x):
        while self.link[x]:
            x = self.link[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return

        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]

class WallGrid:
    def __init__(self, n):
        self.n = n
        self.uf = UnionFind()
        self.rooms = 0

    def remove(self, x, y):
        self.uf.link[(x, y)] = None
        self.uf.size[(x, y)] = 1
        self.rooms += 1
        for i in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if i in self.uf.size:
                if self.uf.find(i) != self.uf.find((x, y)):
                    self.uf.union((x, y), i)
                    self.rooms -= 1

    def count(self):
        return self.rooms

if __name__ == "__main__":
    w = WallGrid(5)
    print(w.count()) # 0
    w.remove(2, 2)
    w.remove(4, 2)
    print(w.count()) # 2
    w.remove(3, 2)
    print(w.count()) # 1
    w.remove(2, 4)
    w.remove(2, 4)
    w.remove(4, 4)
    print(w.count()) # 3
    w.remove(3, 3)
    print(w.count()) # 3
    w.remove(3, 4)
    print(w.count()) # 1

