def count(t):
    count = 0
    sums = [0]
    prevs = dict()

    for i, value in enumerate(t):
        if not sums:
            sums.append(value)
        else:
            sums.append(sums[-1] + value)

        if value not in prevs:
            prevs[value] = dict()
        if sums[-2] not in prevs[value]:
            prevs[value][sums[-2]] = 0
        prevs[value][sums[-2]] += 1

        if sums[-1] in prevs[value]:
            count += prevs[value][sums[-1]]

    return count

if __name__ == "__main__":
    print(count([2,3,-7,2])) # 1
    print(count([1,2,3,4,5])) # 0
    print(count([0,0,0,0,0])) # 15
    print(count([2,1,-2,1,-1,1,-1,1])) # 3
    print(count([1,1,-4,-1,5,-4,2,1])) # 1
    print(count([0]*10**5)) # big
