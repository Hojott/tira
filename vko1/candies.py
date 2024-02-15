def count(a, b, c):
    if a < b:
        return c // a + (c % a) // b
    return c // b + (c % b) // a

if __name__ == "__main__":
    print(count(3, 4, 11)) # 3
    print(count(5, 1, 100)) # 100
    print(count(2, 3, 1)) # 0
    print(count(2, 3, 9)) # 4
