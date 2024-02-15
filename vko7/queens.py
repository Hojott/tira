from math import ceil

def count(n, k):
    if k == 1:
        return n*n
    if k == 2:
        ways = (n*n)**2
        ways -= n*n # place the queen is sitting on
        ways -= n*n * 2*(n-1) # vert and horizontal
        ways -= n*n * (n-1) # 1st diagonal
        for i in range(1, ceil(n/2)):
            ways -= (n-2*i)*(n-2*i) * 2 # 2nd diagonal
        
        return ways
        
                


if __name__ == "__main__":
    print(count(2, 1)) # 4
    print(count(2, 2)) # 0
    print(count(5, 3)) # 204
    print(count(7, 1)) # 49
    print(count(7, 2)) # 700
    print(count(7, 3)) # 3628
