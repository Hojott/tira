def count(t):
    c = 0
    d = dict()
    for i in range(len(t)):
        if not t[i] in d:
            d[t[i]] = []
        
        d[t[i]].append(t[i])
        
        for j in d:
            for k in range(len(d[j])):
                d[j][k] += t[i]

        for j in d[t[i]]:
            if not j:
                c += 1

    return c

if __name__ == "__main__":
    print(count([2,3,-7,2])) # 1
    print(count([1,2,3,4,5])) # 0
    print(count([0,0,0,0,0])) # 15
    print(count([2,1,-2,1,-1,1,-1,1])) # 3
