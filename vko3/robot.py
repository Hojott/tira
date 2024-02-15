def count(s):
    pos = [0,0]
    pos_been = set()
    pos_been.add(tuple(pos))
    for l in s:
        if l == "U":
            pos[1] += 1
        if l == "R":
            pos[0] += 1
        if l == "D":
            pos[1] -= 1
        if l == "L":
            pos[0] -= 1
        
        if tuple(pos) not in pos_been:
            pos_been.add(tuple(pos))

    return len(pos_been)

if __name__ == "__main__":
    print(count("LL")) # 3
    print(count("UUDLRR")) # 5
    print(count("UDUDUDU")) # 2
