import itertools

def count(n, k, x):
    count = 0
    t = list(range(1, n+1))
    numbers_used = set()
    for numbers in itertools.combinations(t, k):
        if tuple(set(numbers)) in numbers_used:
            continue
        numbers_used.add(tuple(set(numbers)))

        if sum(numbers) == x:
            count += 1

    return count

if __name__ == "__main__":
    print(count(1, 1, 1)) # 1
    print(count(5, 2, 6)) # 2
    print(count(8, 3, 12)) # 6
    print(count(10, 4, 20)) # 16
