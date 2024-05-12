from math import factorial

def count(x, coin_list):
    l = [0]*(x+1)
    a = [0]*(x+1)
    l[0] = 1
    for n, v in enumerate(l):
        for c in coin_list:
            if n+c <= x:
                if (not a[n+c]) or a[n]+1 == a[n+c]:
                    l[n+c] += v
                    a[n+c] = a[n]+1
                elif a[n]+1 < a[n+c]:
                    l[n+c] = v
                    a[n+c] = a[n]+1

    return l[x]

if __name__ == "__main__":
    print(count(5, [1, 3, 4])) # 2
    print(count(5, [1])) # 1
    print(count(5, [1, 2, 3, 4])) # 4
    print(count(13, [1, 2, 5])) # 12
    print(count(42, [1, 5, 6, 17])) # 30
