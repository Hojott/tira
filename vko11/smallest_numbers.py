from time import time
from random import randint
from heapq import heappush, heappop

def alg1(biglist):
    sortedlist = sorted(biglist)
    sum = 0

    for i in range(len(sortedlist)//10):
        sum += sortedlist[i]

    return sum

def alg15(biglist):
    sortedlist = sorted(biglist)

    return sum(sortedlist[:len(sortedlist)//10])

def alg2(biglist):
    heaplist = []
    for n in biglist:
        heappush(heaplist, n)

    sum = 0
    for i in range(len(heaplist)//10):
        sum += heaplist[0]
        heappop(heaplist)

    return sum

def alg25(biglist):
    heaplist = []
    for n in range(len(biglist)//10):
        heappush(heaplist, n)

    sum = 0
    for i in range(len(heaplist)):
        sum += heaplist[0]
        heappop(heaplist)

if __name__ == "__main__":

    start = time()
    biglist = [randint(1, 10**9) for _ in range(10**6)]
    print(f"Created list in {time()-start}")

    start = time()
    alg1(biglist)
    print(f"Algorithm 1 in {time()-start}")

    start = time()
    alg2(biglist)
    print(f"Algorithm 2 in {time()-start}")

    start = time()
    alg15(biglist)
    print(f"Algorithm 1.5 in {time()-start}")

    start = time()
    alg25(biglist)
    print(f"Algorithm 2.5 in {time()-start}")

    # Created list in 0.6866440773010254
    # Algorithm 1 in 0.589705228805542
    # Algorithm 2 in 0.35106968879699707
    # Algorithm 1.5 in 0.5636961460113525
    # Algorithm 2.5 in 0.06814408302307129

