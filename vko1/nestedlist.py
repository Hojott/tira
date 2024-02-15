def count(t):
    l = 0
    for i in t:
        if isinstance(i, int):
            l += 1
        if isinstance(i, list):
            l += count(i)
    return l

if __name__ == "__main__":
    print(count([1,2,3])) # 3
    print(count([1,[2,3],4,5,[6]])) # 6
    print(count([1,[1,[1,[1]]]])) # 4
    print(count([[1,2,[3,4]],5,[[6,[7],8]]])) # 8
