from itertools import combinations
from heapq import heappush, heappop
 
def find(n):
    items = []
    prev = set()

    for i in range(n):
        if prev 
        heappush(items, sum(j))
    
    k = 0
    for i in range(n):
        k = heappop(items)
 
    return k

if __name__ == "__main__":
    print(find(1)) # 0
    print(find(2)) # 1
    print(find(3)) # 2
    print(find(4)) # 3
    print(find(5)) # 3
    print(find(123)) # 15
    print(find(123456)) # 62
