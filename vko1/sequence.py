def generate(n):
    thelist = []

    i= 0
    while 1:
        i += 1
        if str(i)[0] == str(i)[-1]:
            thelist.append(i)

        if len(thelist) == n:
            break

    return thelist[-1]


if __name__ == "__main__":
    print(generate(1)) # 1
    print(generate(2)) # 2
    print(generate(3)) # 3
    print(generate(10)) # 11
    print(generate(123)) # 1141
