import itertools

def create(s):
    return sorted(list(map("".join, set(itertools.permutations(s)))))

if __name__ == "__main__":
    print(create("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create("aaaaa")) # ['aaaaa']
    print(create("abab")) # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
    print(len(create("aybabtu"))) # 1260
