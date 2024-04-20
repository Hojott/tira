from time import time
from collections import deque

def push_range(n, deque):
    for i in range(n):
        deque.append(i+1)

def popleft_range(n, deque):
    for i in range(n):
        deque.popleft()

if __name__ == "__main__":
    dq = deque()

    start = time()
    push_range(10**5, dq)
    print(time() - start)

    start = time()
    popleft_range(10**5, dq)
    print(time() - start)


