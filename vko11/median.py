from heapq import heappush, heappop

class Median:
    def __init__(self):
        self.heap = []
        self.antiheap = []

        self.med = None
        self.heaplen = 0

    def add(self, x):
        self.heaplen += 1

        if self.med is None:
            self.med = x
            return

        if x >= self.med:
            heappush(self.heap, x)
        
            if self.heaplen % 2:
                heappush(self.antiheap, -self.med)
                self.med = self.heap[0]
                heappop(self.heap)

        if x < self.med:
            heappush(self.antiheap, -x)

            if not self.heaplen % 2:
                heappush(self.heap, self.med)
                self.med = -self.antiheap[0]
                heappop(self.antiheap)

    def median(self):
        return self.med

if __name__ == "__main__":
    m = Median()
    m.add(1)
    print(m.median()) # 1
    m.add(2)
    print(m.median()) # 1
    m.add(1)
    print(m.median()) # 1
    m.add(3)
    print(m.median()) # 1
    m.add(3)
    print(m.median()) # 2

    print()

    m = Median()
    m.add(10)
    print(m.median()) # 10
    m.add(9)
    print(m.median()) # 9
    m.add(6)
    print(m.median()) # 9
    m.add(10)
    print(m.median()) # 9
    m.add(10)
    print(m.median()) # 10
    m.add(3)
    print(m.median()) # 9
    m.add(6)
    print(m.median())
    m.add(7)
    print(m.median())
    m.add(6)
    print(m.median())
    m.add(5)
    print(m.median())
