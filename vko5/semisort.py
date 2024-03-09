import math

def solve(t):
    count = 0
    spl = math.ceil(len(t) / 2)

    for i, v in enumerate(t):
        if i < spl and v > spl:
            count += (spl-i)
        elif i >= spl and v <= spl:
            count += (i-spl)

    return count

if __name__ == "__main__":
    print(solve([2, 1, 4, 3])) # 0
    print(solve([5, 3, 4, 1, 6, 2])) # 6
    print(solve([6, 5, 4, 3, 2, 1])) # 9
    print(solve([10, 1, 9, 2, 8, 3, 7, 4, 6, 5])) # 15
