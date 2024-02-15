def find(t):
    sm1 = 1000
    sm2 = 1000
    bg1 = 0
    bg2 = 0
    df1 = 0
    df2 = 0
    for i, v in enumerate(t):
        sm1 = min(v, sm1)
        bg1 = max(v, bg1)
        df1 = max(bg1 - sm1, df1)

    return df1


if __name__ == "__main__":
    print(find([1,5,2,1,5])) # 8
    print(find([1,5,1,5])) # 4
    print(find([1,2,3,4,5])) # 4
    print(find([5,4,3,2,1])) # 0
    print(find([4,2,5,8,7,6,1,2,5,1])) # 10
