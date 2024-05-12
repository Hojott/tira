def find(n):
    s = set()
    for i in range(n):

f1 = 0: {} 
f2 = 1: { 1 }
f3 = 2: { 2 }
f4 = 3: { 3 }
f5 = 3: { 1 2 }
f6 = 4: { 4 }
f7 = 4: { 1 3 }
f8 = 5: { 5 }
f9 = 5: { 1 4 }
f10= 5: { 2 3 }
f11= 6: { 6 }
f12= 6: { 1 5 }
f13= 6: { 2 4 }  
f14= 7: { 7 } 
f15= 7: { 1 6 }
f16= 7: { 1 2 4 }
f18= 7: { 2 5 }
f19= 7: { 3 4 }


        

    return sum(s)

if __name__ == "__main__":
    """
    print(find(1)) # 0
    print(find(2)) # 1
    print(find(3)) # 2
    print(find(4)) # 3
    print(find(5)) # 3
    print(find(123)) # 15
    print(find(123456)) # 62
    """
    t = 1
    before = 0
    for i in range(2, 400):
        new = find(i)
        if new == before:
            t += 1
        else:
            before = new
            print(f"{new}: {t}")
            t = 1
