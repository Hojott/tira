def count(a,b,x):
    if a == x or b == x:
        return x
    if a == b:
        return -1

    if b > a:
        a, b = b, a

    water_used = 0
    aw = 0
    bw = 0

    while 1:
        water_used += a
        aw += a
        print(aw, bw, water_used)

        while aw >= b:
            w = b - bw
            water_used += w
            bw += w
            aw -= w
            print(aw, bw, water_used)
            if aw == x or bw == x:
                return water_used

            water_used += bw
            bw -= bw
            print(aw, bw, water_used)

        water_used += aw
        bw += aw
        aw -= aw
        print(aw, bw, water_used)
        if aw == x or bw == x:
            return water_used


if __name__ == "__main__":
    print(count(5, 4, 2)) # 22
    print(count(4, 3, 2)) # 16
    print(count(3, 3, 1)) # -1
    print(count(10, 9, 8)) # 46
    #print(count(123, 456, 42)) # 10530
