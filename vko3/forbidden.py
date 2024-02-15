def count(s):
    c = 0
    a = -1 # a is always on latest 'a'
    for i in range(len(s)):
        if s[i] == 'a':
            a = i
        else:
            c += i - a
    return c
        

if __name__ == "__main__":
    print(count("aaa")) # 0
    print(count("saippuakauppias")) # 23
    print(count("x")) # 1
    print(count("aybabtu")) # 9
