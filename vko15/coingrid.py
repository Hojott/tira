from itertools import permutations

def way(coins, rows, columns, perm):
    deleted = set()
    i = 0
    while coins != deleted and i < len(perm):
        now = perm[i]
        i += 1

        l = rows
        if now >= len(rows):
            l = columns
            now -= len(rows)

        deleted.update(l[now])
        l[now] = set()

    return i


def count(r):
    coins = set()

    rows = []
    for _ in range(len(r)):
        rows.append(set())

    columns = []
    for _ in range(len(r[0])):
        columns.append(set())

    for x, row in enumerate(r):
        for y, square in enumerate(row):
            if square == ".":
                continue
            coins.add((x, y))
            rows[x].add((x, y))
            columns[y].add((x, y))

    alles = []
    for i, s in enumerate(rows+columns):
        if s:
            alles.append(i)

    smallest = float('inf')
    for perm in permutations(alles):
        smallest = min(smallest, way(coins, rows, columns, perm))

    return smallest


if __name__ == "__main__":
    r =["..X",
        "..."]
    print(count(r)) # 1

    r =["........",
        "........",
        "...X..X.",
        "........",
        "....X...",
        "..X.X..X",
        "........",
        "....X..."]
    print(count(r)) # 3

    r =[".....",
        "...X.",
        ".....",
        "X....",
        "....."]
    print(count(r)) # 2

    r =[".......",
        "...X...",
        ".X.....",
        ".....X.",
        "...X...",
        "......X",
        ".X....X"]
    print(count(r)) # 4
