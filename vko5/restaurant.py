def find(a, d):
    timeline = dict()
    for v in a:
        if v in timeline:
            timeline[v][0] += 1
        else:
            timeline[v] = [1, 0]

    for v in d:
        if v in timeline:
            timeline[v][1] += 1
        else:
            timeline[v] = [0, 1]

    people = 0
    streak_start = 0
    longest = 0
    for k in sorted(timeline):
        people += timeline[k][0]

        if people and streak_start:
            longest = max(longest, k - streak_start)
            streak_start = 0
        
        people -= timeline[k][1]

        if not people and not streak_start:
            streak_start = k

    return longest

if __name__ == "__main__":
    print(find([1, 6], [2, 9])) # 4
    print(find([1, 2, 3], [2, 3, 4])) # 0
    print(find([1, 4, 6, 8], [5, 5, 9, 9])) # 1
    print(find([1, 10**9], [2, 10**9+1])) # 999999998
    print(find([9,7,5,1,6,6,10,8], [12,12,5,2,7,11,10,9])) # 3
