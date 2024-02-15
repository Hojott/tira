def binary_search(items, x):
    left = 0
    right = len(items) - 1

    while left < right:
        middle = (left + right) // 2

        if items[middle] == x:
            return True

        if items[middle] > x:
            right = middle - 1
        else:
            left = middle + 1

    return False

numbers = [1, 3, 8]

print(binary_search(numbers, 8)) # True
print(binary_search(numbers, 3)) # True
print(binary_search(numbers, 4)) # False
