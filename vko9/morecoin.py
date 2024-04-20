def count(x):
    sum = 0

    print("-", x)

    sum += (x % 5) % 4
    x -= (x % 5) % 4

    print("-", x)

    sum += (x % 5) // 4
    x -= x % 5

    print("-", x)

    sum += x//5

    return sum

if __name__ == "__main__":
    for i in range(22):
        print(i, ":", count(i))
    #print(count(8)) # 2
    #print(count(12345)) # 2469
    #print(count(1337**9)) # 2730314408854633746890878156
