import collections

def solve(n,k):
    queue = collections.deque(range(1, n+1))

    for i in range(k):
        n1 = queue.popleft()
        n2 = queue.popleft()

        queue.append(n2)
        queue.append(n1)
    
    return queue.popleft()

if __name__ == "__main__":
    print(solve(4, 3)) # 4
    print(solve(12, 5)) # 11
    print(solve(99, 555)) # 11
    print(solve(12345, 54321)) # 9875
