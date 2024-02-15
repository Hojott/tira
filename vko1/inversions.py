def count(t):
    sum = 0
    for i, ti in enumerate(t):
        for j, tj in enumerate(t):
            if ti > tj and i < j:
                sum += 1
        #if i == j:
        #    continue

    return sum


if __name__ == "__main__":
    print(count([1,3,2])) # 1
    print(count([1])) # 0
    print(count([4,3,2,1])) # 6
    print(count([1,8,2,7,3,6,4,5])) # 12
    print(count([6, 7, 5, 8, 9, 1, 2, 3, 4])) # 34
