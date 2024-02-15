def count(t):
    c = 0
    d = 0
    first = 0
    last = 0
    for i in range(len(t)):
        if t[i] < t[first]:
            first = i
        if t[i] == t[first]:
            last = i

    if last - first > 0:
        return last - first
    return 0

if __name__ == "__main__":
    print(count([2,1,1,3])) # 1
    print(count([1,1,1,1])) # 3
    print(count([1,2,3,1,2,3])) # 3
    print(count([1,2,3,4,3,2,1])) # 6
    print(count([4,3,2,1,2,3,4])) # 0
