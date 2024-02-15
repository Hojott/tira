import time
import random

def count_even_slow(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

def count_even_fast(numbers):
    return sum(x % 2 == 0 for x in numbers)

def perf_test(rounds):
    slow_ones = []
    fast_ones = []

    for i in range(rounds):
        print(f"{int(i/rounds * 100)}% done...  ", end="\r")
        rand = random.sample(range(1, 10**8), 10**7)

        start = time.time()
        count_even_slow(rand)
        end = time.time()
        slow_ones.append(end - start)

        start = time.time()
        count_even_fast(rand)
        end = time.time()
        fast_ones.append(end - start)

    slow_results = sum(slow_ones) / rounds
    fast_results = sum(fast_ones) / rounds

    print("First test:", slow_results)
    print("Second test:", fast_results)

if __name__ == "__main__":
    perf_test(10)
