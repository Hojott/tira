# Slightly modified from robotroute
def poscount(s,start,pos_been):
    pos = start
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
 
    return (len(pos_been), pos, pos_been)

def count(s, k):
    (firstv, pos, pos_been) = poscount(s, [0,0], set())
    
    diffs = [firstv]
    nextv = firstv

    """
    for i in range(k):
        prevv = nextv

        (nextv, pos, pos_been) = poscount(s, pos, pos_been)
        print(prevv, nextv)

        if nextv - prevv == diffs[-1]:
            break

        diffs.append(nextv - prevv)
    """

    for i in range(len(s+"1")):
        prevv = nextv

        (nextv, pos, pos_been) = poscount(s, pos, pos_been)

        diffs.append(nextv - prevv)


    return sum(diffs) + (diffs[-1]) * (k-len(diffs))

if __name__ == "__main__":
    #print(count("UR", 100)) # 201
    #print(count("UD", 100)) # 2
    #print(count("UURRDDL", 500)) # 1506
    #print(count("L", 10**9)) # 1000000001
    #print(count("DLUR", 10**9)) # 4
    #print(count("LDLRDRRRUU", 3)) # 23
    print(count("UURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL", 1000000000)) # 3000000144
