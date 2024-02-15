def find(t, k):
    ts = sorted(t)
    first = 1 - (ts[0] - 1) # theres a good reason for this thats hard to explain
    ts.insert(0, first)
    last = k + (k - ts[-1])
    ts.append(last)

    longest = 0
    for i in range(1, len(ts)):
        longest = max(longest, ts[i] - ts[i-1])

    return longest//2

if __name__ == "__main__":
    print(find([1, 2, 9], 11)) # 3
    print(find([2, 1, 3], 3)) # 0
    print(find([7, 4, 10, 4], 10)) # 3
    print(find([15, 2, 6, 4, 18], 20)) # 4
    print(find([41222388, 392676742, 307110407, 775934683, 25076911], 809136843)) # 191628970
