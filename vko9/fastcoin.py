def count(x):
    coin5 = x // 5
    coin2 = (x%5) // 2
    coin1 = (x%5)%2
    return coin1+coin2+coin5

if __name__ == "__main__":
    print(count(13)) # 4
    print(count(12345)) # 2469
    print(count(1337**9)) # 2730314408854633746890878156
