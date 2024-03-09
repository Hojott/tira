def count(s):
    count = 0
    d = {"t": None, "i": None, "r": None, "a": None}

    def all():
        return d["t"] is not None and d["i"] is not None and d["r"] is not None and d["a"] is not None

    def smallest():
        return min(d["t"], d["i"], d["r"], d["a"])

    def greatest():
        return max(d["t"], d["i"], d["r"], d["a"])
    
    for i, v in enumerate(s):
        if v in d:
            d[v] = i

        if all():
            count += smallest() - (-1)# + i - greatest()

        #print(v, count)

    return count

if __name__ == "__main__":
    print(count("aybabtu")) # 0
    print(count("tira")) # 1
    print(count("ritari")) # 6
    print(count("tiratiratira")) # 45
    print(count("xaxrxixtx")) # 4
