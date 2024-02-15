def count(s):
    c = 0
    a = 0
    for i in range(len(s)):
        if s[i] != s[a]:
            a = i
        c += i - a + 1
    return c
        

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5
