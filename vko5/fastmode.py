class FastMode:
    def __init__(self):
        self.d = dict()
        self.m = [0,0]

    def add(self, x, k):
        if x not in self.d:
            self.d[x] = 0
        self.d[x] += k
        
        if self.d[x] > self.m[1] or (self.d[x] == self.m[1] and x < self.m[0]):
            self.m = [x, self.d[x]]

    def mode(self):
        return self.m[0]

if __name__ == "__main__":
    m = FastMode()
    m.add(4, 7)
    print(m.mode()) # 4
    m.add(8, 5)
    print(m.mode()) # 4
    m.add(8, 3)
    print(m.mode()) # 8
    m.add(4, 1)
    print(m.mode()) # 4
