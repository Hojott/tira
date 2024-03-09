def count(t):
    count = 0
    sums = []
    prevs = dict()

    for i, value in enumerate(t):
        modified = False

        if value not in prevs:
            prevs[value] = [[i, 1]]
            modified = True

        if not sums:
            sums.append(value)
        else:
            sums.append(sums[-1] + value)

        
        for prev in reversed(prevs[value]):
            j = prev[0]
            c = prev[1]
            if (j != 0 and sums[i] - sums[j-1] == 0) \
            or (j == 0 and sums[i] == 0):
                count += c
                #prev[1] += 1 # c += 1
                modified = True
        
        if not modified:
            prevs[value].append([i, 1])
        
        print(sorted(prevs.items()), count)

    return count

if __name__ == "__main__":
    print(count([2,3,-7,2])) # 1
    print(count([1,2,3,4,5])) # 0
    print(count([0,0,0,0,0])) # 15
    print(count([2,1,-2,1,-1,1,-1,1])) # 3
