def count(s):
    c = 0
    l = 0
    d = {"t": -1, "i": -1, "r": -1, "a": -1}
    for i in range(len(s)):
        lastmin = min(d.values())
        if s[i] in d and d[s[i]] == -1:
            d[s[i]] = i
        if lastmin != min(d.values()):
            l = lastmin
        if min(d.values()) >= 0:
            c += min(d.values()) - l
    return c

if __name__ == "__main__":
    print(count("aybabtu")) # 0
    print(count("tira")) # 1
    print(count("ritari")) # 6
    print(count("tiratiratira")) # 45
    print(count("xaxrxixtx")) # 4
