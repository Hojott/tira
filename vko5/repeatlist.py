class RepeatList:
    def __init__(self):
        self.s = set()
        self.true = False

    def add(self, x):
        if x in self.s:
            self.true = True
        self.s.add(x)

    def check(self):
        return self.true

if __name__ == "__main__":
    r = RepeatList()
    print(r.check()) # False
    r.add(1)
    r.add(2)
    r.add(3)
    print(r.check()) # False
    r.add(2)
    print(r.check()) # True
    r.add(5)
    print(r.check()) # True
