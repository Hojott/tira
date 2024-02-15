import time

def count(a, b):
    n = len(a)
    positions = [0] * (n+1)
    for i in range(n):
        positions[b[i]] = i
    result = 0
    for i in range(n):
        if i < positions[a[i]]:
            result += 1
    return result

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
