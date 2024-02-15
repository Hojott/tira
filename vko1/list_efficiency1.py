import time

def add_list(l, n):
    for i in range(n):
        l.append(i)

def rm_list(l, n):
    for i in range(n):
        l.pop()

def test():
    l = []
    n = 10**5

    start = time.time()
    add_list(l, n)
    end = time.time()
    print("Time to append:", end - start)

    start = time.time()
    rm_list(l, n)
    end = time.time()
    print("Time to pop:", end - start)

if __name__ == "__main__":
    test()
