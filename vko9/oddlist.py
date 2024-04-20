import itertools

def count(n, x):
    count = 0
    t = list(range(1, n+1))
    for permutation in itertools.permutations(t):
        if valid_permutation(permutation, x):
            count += 1
    return count

def valid_permutation(permutation, x):
    if permutation[0] != x:
        return False
    sums = set()

    for i, right in enumerate(permutation[1:]):
        left = permutation[i] # pretty ugly but works
        if left + right in sums:
            return False
        sums.add(left+right)

    return True

if __name__ == "__main__":
    print(count(1, 1)) # 1
    print(count(4, 2)) # 4
    print(count(8, 5)) # 830
