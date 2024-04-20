from heapq import heappush, heappop

def smallest(n):
    keko = []
    heappush(keko, 1)

    for i in range(n):
        num = keko[0]
        heappop(keko)
        heappush(keko, num*2)
        heappush(keko, num*3)

    return keko[0]

if __name__ == "__main__":
    print(smallest(1)) # 2
    print(smallest(5)) # 6
    print(smallest(123)) # 288
    print(smallest(55555)) # 663552
