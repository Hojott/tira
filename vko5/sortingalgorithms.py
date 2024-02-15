import time
import random

def swap(items, a, b):
    temp = items[a]
    items[a] = items[b]
    items[b] = temp

def insertion_sort(items):
    for i in range(1, len(items)):
        for j in range(i - 1, -1, -1):
            if items[j] > items[j + 1]:
                swap(items, j, j + 1)
            else:
                break

def merge_sort(items):
    n = len(items)

    if n == 1: return

    left = items[0:n//2]
    right = items[n//2:]

    merge_sort(left)
    merge_sort(right)

    a = b = 0
    for i in range(n):
        if b == len(right) or \
           (a < len(left) and left[a] < right[b]):
            items[i] = left[a]
            a += 1
        else:
            items[i] = right[b]
            b += 1

def python_sort(items):
    items.sort()

def time_sorting(fsort, n=100000):
    sample = list(range(1, n+1))
    random.shuffle(sample)
    print("Shuffled", end="\r")
    start = time.time()
    fsort(sample)
    end = time.time()
    print("Sorted  ", end="\r")

    # Non-memoryefficient?
    if list(range(1, n+1)) == sample:
        return end - start
    raise Exception

if __name__ == "__main__":
    # Too long, gotta use math or something
    time1 = time_sorting(insertion_sort, n=10000)
    print("Insertion sort:", time1*100)

    time2 = time_sorting(merge_sort)
    print("Merge sort:", time2)

    time3 = time_sorting(python_sort)
    print("Python sort:", time3)
