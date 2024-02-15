def count(t):
    c = 0
    a = -1
    d = dict()
    for i in range(len(t)):
        if t[i] in d:
            a = max(d[t[i]], a)
            d[t[i]] = i
        
        d[t[i]] = i
        c += i - a

    return c

if __name__ == "__main__":
    print(count([1,2,3,4])) # 10
    print(count([1,1,1,1])) # 4
    print(count([5])) # 1
    print(count([1,3,2,3,4,2,4,1,2,1])) # 24
