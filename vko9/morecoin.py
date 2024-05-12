def count(x):

    leftover = x % 5

    if x == 3:
        plus = 3
    elif leftover == 2 and x < 10:
        plus = 2
    elif leftover == 0:
        plus = 0
    else:
        plus = 1

    return x // 5 + plus


if __name__ == "__main__":
    print(count(8)) # 2
    print(count(12345)) # 2469
    print(count(1337**9)) # 2730314408854633746890878156
