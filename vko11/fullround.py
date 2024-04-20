import collections

def count(n):
    """
    queue = collections.deque(range(1, n+1))
    queuecp = collections.deque(range(1, n+1))

    for i in range(n**5):
        print(queue)
        n1 = queue.popleft()
        n2 = queue.popleft()

        queue.append(n2)
        queue.append(n1)

        if queue == queuecp:
            print(queue)
            return i+1
    """

    if n % 2:
        parilliset = n // 2
        parittomat = n - parilliset
        return parilliset * parittomat
    else:
        return n

if __name__ == "__main__":
    print(count(2)) # 2
    print(count(5)) # 6
    print(count(6)) # 6
    print(count(31)) # 240
    print(count(32)) # ?
    print(count(1234567)) # 381038919372
