def find(t):
    n = len(prices)
    best1 = 0
    best2 = 0
    min_price1 = prices[0]
    min_price2 = prices[0]
    for i in range(n):
        min_price = min(min_price, prices[i])
        best = max(best, prices[i] - min_price)
    return best


if __name__ == "__main__":
    print(find([1,5,2,1,5])) # 8
    print(find([1,5,1,5])) # 4
    print(find([1,2,3,4,5])) # 4
    print(find([5,4,3,2,1])) # 0
    print(find([4,2,5,8,7,6,1,2,5,1])) # 10
