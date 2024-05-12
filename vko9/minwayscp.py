from math import factorial

def count(x, coin_list):
    sets = [{0}]
    count = 0
    for i in range(x):
        nl = set()
        for j in sets[i]:
            for k in coin_list:
                if j+k > x:
                    continue
                if j+k == x:
                    count += 1
                
                nl.add(j+k)

        sets.append(nl)
        if count:
            break

    return count
        
        

if __name__ == "__main__":
    print(count(5, [1])) # 1
    print(count(5, [1, 2, 3, 4])) # 4
    print(count(13, [1, 2, 5])) # 12
    print(count(42, [1, 5, 6, 17])) # 30
