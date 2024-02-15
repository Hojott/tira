def find(t):
    firstnum = 0
    secondnum = 0
    amount1 = 0
    amount2 = 0
    for (i, num) in enumerate(t):
        if i == 0:
            firstnum = num
        
        if num == firstnum:
            amount1 += 1
        else:
            secondnum = num
            amount2 += 1
    
    return firstnum if amount1 < amount2 else secondnum

if __name__ == "__main__":
    print(find([1,1,2,1])) # 2
    print(find([4,5,5])) # 4
    print(find([1,1,1,1,2])) # 2
    print(find([8,8,5,8,8])) # 5
