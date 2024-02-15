class MaxList:
    def __init__(self):
        self.l = []
        self.largest = None

    def add(self, x):
        self.l.append(x)
        if self.largest is None:
            self.largest = x
        else:
            self.largest = max(self.largest, x)

    def max(self):
        return self.largest
        

if __name__ == "__main__":
    m = MaxList()
    print(m.max()) # None
    m.add(1)
    m.add(2)
    m.add(3)
    print(m.max()) # 3
    m.add(8)
    m.add(5)
    print(m.max()) # 8
