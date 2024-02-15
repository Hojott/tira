def find(t):
    indexes = dict()
    for i, v in enumerate(t):
        if not v in indexes:
            indexes[v] = i

    length = 0
    for i, v in enumerate(reversed(t)):
        nlen = len(t) - i - indexes[v] - 1
        if nlen > length:
            length = nlen

    return length


if __name__ == "__main__":
    print(find([1,2,1,1,2])) # 3
    print(find([1,2,3,4])) # 0
    print(find([1,1,1,1,1])) # 4
    print(find([1,1,2,3,4])) # 1
    print(find([1,5,1,5,1])) # 4
