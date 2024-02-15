def count(t):
    ts = sorted(t)
    longest = 1
    combo = 1

    for i in range(1, len(ts)):
        if ts[i] == ts[i-1]:
            continue
        if ts[i] - ts[i-1] == 1:
            combo += 1
        else:
            longest = max(longest, combo)
            combo = 1

    longest = max(longest, combo)
    return longest


        


if __name__ == "__main__":
    print(count([1, 1, 1, 1])) # 1
    print(count([10, 4, 8])) # 1
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    print(count([987654, 12345678, 987653, 999999, 987655])) # 3
