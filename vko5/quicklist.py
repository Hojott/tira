class QuickList:
    def __init__(self, t):
        self.t = t.copy()
        self.id = list(range(len(t)))
        self.offset = 0

    def move(self, k):
        for i in range(k):
            self.id[(i + self.offset) % len(self.id)] += len(self.id)# - self.offset
        self.offset += k

    def get(self, i):
        #print(self.t, self.id, self.offset)
        return self.t[(self.id[i] + self.offset) % len(self.id)]

if __name__ == "__main__":
    q = QuickList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(q.get(4)) # 5
    q.move(3)
    print(q.get(4)) # 8
    q.move(3)
    print(q.get(4)) # 1
    q.move(10)
    print(q.get(4)) # 1
    q.move(7)
    q.move(5)
    print(q.get(0)) # 9
