def count(n, k):
    ways = set()

    for (x1, y1) in [(i, j) for i in range(1, n+1) for j in range(1, n+1)]:
        if k == 1:
            ways.add(((x1, y1)))
            continue

        for (x2, y2) in [(i, j) for i in range(1, n+1) for j in range(1, n+1)]:
            if x1 == x2 or y1 == y2: # vert and horizontal
                continue
            if x1 - y1 == x2 - y2: # diagonal
                continue
            if (n-x1) - y1 == (n-x2) - y2:
                continue

            if k == 2:
                way = sorted([(x1, y1), (x2, y2)], key=lambda x: x[0])
                ways.add(tuple(way))
                continue

            for (x3, y3) in [(i, j) for i in range(1, n+1) for j in range(1, n+1)]:
                if x3 == x2 or x3 == x1 or y3 == y1 or y3 == y2:
                    continue
                if x3 - y3 == x2 - y2 or x3 - y3 == x1 - y1:
                    continue
                if (n-x3) - y3 == (n-x2) - y2 or (n-x3) - y3 == (n-x1) - y1:
                    continue

                way = sorted([(x1, y1), (x2, y2), (x3, y3)], key=lambda x: x[0])
                ways.add(tuple(way))

    return len(ways)

if __name__ == "__main__":
    print(count(2, 1)) # 4
    print(count(2, 2)) # 0
    print(count(5, 3)) # 204
    print(count(7, 1)) # 49
    print(count(7, 2)) # 700
    print(count(7, 3)) # 3628
