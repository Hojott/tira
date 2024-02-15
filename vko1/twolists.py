import time

def count(a, b):
    amount = 0
    #delta = 0
    b_set = set()
    for i in range(len(a)):
        b_set.add(b[i])
        if a[i] not in b_set:
            amount += 1

        #if a[i] not in set(b[0:i+1-delta]):
        #    amount += 1
        #    continue

        #b.remove(a[i])
        #delta += 1

    return amount


if __name__ == "__main__":
    #print(count([2,3,4,1], [1,2,3,4])) # 3
    #print(count([1,2,3,4], [1,2,3,4])) # 0
    #print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    #print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5
    #print(count([2, 1, 4, 3, 5], [1, 2, 5, 4, 3])) # 3

    a = list(range(1, 10**8 + 1))
    b = list(range(1, 10**8 + 1))
    start = time.time()
    print(count(a,b))
    end = time.time()
    print(end-start)
