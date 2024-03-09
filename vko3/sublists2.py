def count(t):
    count = 0
    sums = []
    prevs = dict()

    for i, value in enumerate(t):
        if value not in prevs:
            prevs[value] = []
        prevs[value].append([i, 0])

        if not sums:
            sums.append(value)
        else:
            sums.append(sums[-1] + value)

        to_remove = []
        for index, (j, w) in enumerate(prevs[value]):
            sublist = False

            if j == 0 and sums[i] == 0:
                """ When we're targeting the first value """
                sublist = True
                print("ah")
            elif j != 0 and sums[i] - sums[j-1] == 0 and w == 0:
                """ When we're targeting something with no weight """
                sublist = True
                print("aah")

            if i == j:
                if value == 0:
                    count += 1

                count += prevs[value][-1][1] # w
            
            elif sublist:
                prevs[value][-1][1] += w+1
                to_remove.append(index)
            
        for j, index in enumerate(to_remove):
            prevs[value].pop(index-j)

        print(prevs, count)

    return count

if __name__ == "__main__":
    #print(count([2,3,-7,2])) # 1
    #print(count([1,2,3,4,5])) # 0
    print(count([0,0,0,0,0])) # 15
    print(count([2,1,-2,1,-1,1,-1,1])) # 3
    print(count([1,1,-4,-1,5,-4,2,1])) # 1
    #print(count([0]*10**5)) # big
