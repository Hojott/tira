class TrackRepeat:
    def __init__(self):
        self.coolset = set()
        self.cooldict = dict()
        self.false = dict()

    def add(self, x, k):
        if not x in self.cooldict:
            self.cooldict[x] = 0
        
        # just for clean code
        xk = self.cooldict[x]

        if xk in self.false:
            self.false[xk] -= 1
            if not self.false[xk]:
                del self.false[xk]
        else:
            self.coolset.discard(xk)
            
        self.cooldict[x] += k
        # reassign cause python hasnt got pointers
        xk = self.cooldict[x]

        if xk in self.coolset:
            if xk not in self.false:
                self.false[xk] = 0
            self.false[xk] += 1

        self.coolset.add(xk)


    def check(self):
        return not self.false

if __name__ == "__main__":
    t = TrackRepeat()
    print(t.check()) # True
    t.add(1, 3)
    print(t.check()) # True
    t.add(2, 3)
    print(t.check()) # False
    t.add(2, 2)
    print(t.check()) # True
    t.add(3, 1)
    print(t.check()) # True
    t.add(3, 4)
    print(t.check()) # False

    print()

    t = TrackRepeat()
    t.add(10, 3)
    print(t.check())
    t.add(6, 8)
    print(t.check())
    t.add(10, 4)
    print(t.check())
    t.add(1, 2)
    print(t.check())
    t.add(9, 2)
    print(t.check())
    t.add(10, 1)
    print(t.check())
    t.add(3, 3)
    print(t.check())
    t.add(7, 6)
    print(t.check())
    t.add(9, 6)
    print(t.check())
    t.add(9, 2)
    print(t.check())

