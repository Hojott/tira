import random

def create(n):
    l = []
    numbers = [i+1 for i in range(n)]
    for i in range(n):
        for j in range(n):
            l.append(numbers[j])
            if len(l) > 2 and l[-1]+l[-2] in [l[k]+l[k-1] for k in range(len(l)-1)]:
                l.pop()
                continue
            numbers.pop(j)
            break

    return l




if __name__ == "__main__":
    print(create(6)) # [3, 1, 6, 2, 4, 5]
    print(create(10)) # [7, 10, 3, 1, 5, 4, 8, 6, 9, 2]
    print(create(15)) # [9, 4, 6, 14, 15, 13, 12, 11, 5, 2, 3, 8, 1, 7, 10]
