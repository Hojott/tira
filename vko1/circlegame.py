def create(n):
    ln = [i+1 for i in range(n)]
    l = []
    i = 1
    while 1:
        if len(l) == n:
            break

        try:
            l.append(ln.pop(i))
        except IndexError:
            ln_copy = []
            for j in ln:
                if j not in l and j not in ln_copy:
                    ln_copy.append(j)

            ln += ln_copy
            i -= 1

        i += 1
    return l
            

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2,1,3]
    print(create(4)) # [2,4,3,1]
    print(create(7)) # [2,4,6,1,5,3,7]
