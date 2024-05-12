import itertools

def create(n, i=0, t=[], used=set()):
    if i == 0:
        t = [0]*n
        used = set()

    usedcp = used.copy()
    for j in range(1, n+1):
        used = usedcp.copy()
        if t[-1] != 0:
            return t

        if (i != 0 and (j+1 == t[i-1] or j-1 == t[i-1])) or j in used:
            continue

        t[i] = j
        used.add(t[i])

        
        create(n, i=i+1, t=t, used=used)
        
    if t[-1] != 0:
        return t
    return None


if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(2)) # None
    print(create(4)) # [2, 4, 1, 3]
    print(create(7)) # [1, 3, 5, 2, 6, 4, 7]
    print(create(10)) # [1, 3, 5, 2, 4, 6, 8, 10, 7, 9]
