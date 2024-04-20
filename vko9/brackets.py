import itertools

def count(n, k):
    count = 0
    for sequence in itertools.product("()", repeat=n):
        if valid_sequence(sequence, k):
            count += 1
    return count

def valid_sequence(sequence, k):
    depth = 0
    for bracket in sequence:
        if depth > k:
            return False
        if bracket == "(":
            depth += 1
        if bracket == ")":
            depth -= 1
        if depth < 0:
            return False
    return depth == 0

if __name__ == "__main__":
    print(count(6, 1)) # 1
    print(count(6, 2)) # 4
    print(count(6, 3)) # 5
    print(count(9, 1)) # 0
    print(count(16, 4)) # 1094
