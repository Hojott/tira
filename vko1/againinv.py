def create(n, k):
    l = [i+1 for i in range(n)]
    i = 0
    j = 0
    counter = 0
    while i < k:
        if j == n-1-counter:
            j = 0
            counter += 1
            continue
        hold = l[j]
        l[j] = l[j+1]
        l[j+1] = hold

        j += 1
        i += 1

    return l


if __name__ == "__main__":
    print(create(3, 0)) # [1,2,3]
    print(create(3, 1)) # esim. [1,3,2]
    print(create(3, 2)) # esim. [3,1,2]
    print(create(9, 34))
