from math import sqrt

class SquareSum:
    def __init__(self):
        self.y = 0 # sum of y
        self.ys = 0 # sum of y squared

        self.x = 0
        self.xs = 0

        self.yx = 0
        self.n = 0 # how many points there are

        # (y - (ax + b))²
        # ((y-b) - ax)²
        # (y-b)² - 2(y-b)ax + (ax)²
        # (y² - 2yb + b²) - 2(y-b)ax + a²x²
        # + (y2² - 2y2b + b²) - 2(y2-b)ax2 + a²x2²
        # = ((y²+y2²) - (2yb + 2y2b) + (b²+b²)) - (2(y-b)ax + 2(y2-b)ax2) + (a²x² + a²x2²)
        # = (y²+y2²) - (2b(y+y2)) + (2b²) - (2a((y-b)x)+(y2-b)x2) + (a²(x+x2)²)
        # = ... - 2a(yx - bx + y2x2 - bx2) + ...
        # = ... - 2a(yx + y2x2 - b(x+x2))

    def add(self, x, y):
        self.y += y
        self.ys += y**2

        self.x += x
        self.xs += x**2

        self.yx += y*x
        self.n += 1

    def calc(self, a, b):
        h1 = self.ys
        h2 = 2 * b * self.y
        h3 = self.n * b**2
        h4 = 2 * a * (self.yx - b * self.x)
        h5 = a**2 * self.xs

        return (h1 - h2 + h3) - h4 + h5

if __name__ == "__main__":
    s = SquareSum()
    s.add(1, 1)
    s.add(3, 2)
    s.add(5, 3)
    print(s.calc(1, 0)) # 5
    print(s.calc(1, -1)) # 2
    print(s.calc(0.5, 0.5)) # 0
    s.add(4, 2)
    print(s.calc(0.5, 0.5)) # 0.25
