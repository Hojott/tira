import time
import random

class AnalysisMex:
    def __init__(self):
        self.seen = set()
        self.mex = 0

    def add(self, x):
        self.seen.add(x)
        while self.mex in self.seen:
            self.mex += 1
        return self.mex

class Mex:
    def __init__(self):
        self.s = set()
        self.mex = 0

    def add(self, x):
        self.s.add(x)
        if self.mex == x:
            while self.mex in self.s:
                self.mex += 1

        return self.mex

if __name__ == "__main__":
    a = AnalysisMex()
    m = Mex()

    sample = 10**8
    rand = [random.randint(0, sample) for _ in range(sample)]
    
    start = time.time()
    for i in range(sample):
        a.add(rand[i])
    print(time.time() - start)
    
    start = time.time()
    for i in range(sample):
        m.add(rand[i])
    print(time.time() - start)
