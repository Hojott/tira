def count(t):
    d = dict()
    cases = 0
    for i, v in enumerate(t):
        # increment dict
        if not v in d:
            d[v] = 0
        d[v] += 1
        
        # cases that can be dismissed
        if v % 2 or not v // 2 in d:
            continue

        # aaaaaaAH
        cases += d[v // 2]

    return cases

if __name__ == "__main__":
    print(count([1,2,3,4])) # 2
    print(count([1,1,1,1])) # 0
    print(count([1,2,1,2,1,2])) # 6
    print(count([5,1,3,4,1,6])) # 1
    print(count([5,3,5,5,2,3,4,3,3,4])) # 2
