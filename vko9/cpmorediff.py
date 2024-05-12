import itertools

def create(n):
    t = list(range(1, n+1))
    smallest = None
    for permutation in itertools.permutations(t):
        if ( smallest is None or list(permutation) < smallest ) and valid_permutation(permutation):
            if smallest is None:
                smallest = list(permutation)
            else:
                smallest = min(list(permutation), smallest)
    return smallest

def valid_permutation(permutation):
    for i, right in enumerate(permutation[1:]):
        left = permutation[i] # pretty ugly but works
        if left == right+1 or left == right-1:
            return None

    return permutation

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(2)) # None
    print(create(4)) # [2, 4, 1, 3]
    print(create(7)) # [1, 3, 5, 2, 6, 4, 7]
    print(create(10)) # [1, 3, 5, 2, 4, 6, 8, 10, 7, 9]
