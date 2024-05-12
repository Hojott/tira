from math import factorial, comb, log10, floor

def ncr(n, k, cache={}):
    """ comb wrapper with cache """
    if (n, k) in cache:
        return cache[(n, k)]

    ans = comb(n, k)
    cache[(n, k)] = ans
    return ans

def count(x, debug=True):
    if x < 40 or x > 64:
        if debug:
            print("wt:", 0)
        return 0, 0

    fac = factorial(x)
    
    def base(n):
        """ [ 0 ... x-40-n ... 8 ]
        Basically from what step it should start and increments on each above until 8 """
        return min(max(x-40-n, 0), 8)

    wt =  ncr(8, 5) ** (   8    - base(1))  * ncr(8,    8   -base(0))
    wt *= ncr(8, 6) ** (base(0) - base(8))  * ncr(8, base(0)-base(8))
    wt *= ncr(8, 7) ** (base(1) - base(16)) * ncr(8, base(1)-base(16))
    wt *= ncr(8, 8) ** (base(2) - base(24)) * ncr(8, base(2)-base(24))

    if debug:
        print("wt:", wt)

    return fac*wt, wt


if __name__ == "__main__":

    for i in range(40, 65):
        c, _ = count(i, debug=False)
        print(floor(log10(c)), end=" ")    
    print("\n")
    
    for i in range(40, 65):
        _, wt = count(i, debug=False)
        print(floor(log10(wt)), end=" ")    
    print("\n")

    c, _ = count(40)
    print(c) # 78913132667888442497725132524762783866832203758436352000000000
    print(c == 78913132667888442497725132524762783866832203758436352000000000)
    print()

    c, _ = count(41)
    print("wt:", ncr(8, 5) ** 7 * ncr(8, 6) ** 1 * ncr(8, 1), "should")
    print(c) # 78913132667888442497725132524762783866832203758436352000000000
    #print(c == 78913132667888442497725132524762783866832203758436352000000000)
    print()

    c, _ = count(42)
    print("wt:", 1106519946269131740703101808262223755380721161100794527744000000000//factorial(42), "should")
    print(c) # 1106519946269131740703101808262223755380721161100794527744000000000
    print(c == 1106519946269131740703101808262223755380721161100794527744000000000)
    print("log:", floor(log10(1106519946269131740703101808262223755380721161100794527744000000000)))
    print()

    c, _ = count(55)
    print(c) # 320424698352073967965876852452014215914220727801318938295395908593909760000000000000
    print(c == 320424698352073967965876852452014215914220727801318938295395908593909760000000000000)
    print("log:", floor(log10(320424698352073967965876852452014215914220727801318938295395908593909760000000000000)))
    print()

    c, _ = count(63)
    print("wt:", ncr(8, 7) * ncr(8, 1), "should")
    print(c) # 126886932185884164103433389335161480802865516174545192198801894375214704230400000000000000
    #print(c == 126886932185884164103433389335161480802865516174545192198801894375214704230400000000000000)
    print()

    c, _ = count(64)
    print(c) # 126886932185884164103433389335161480802865516174545192198801894375214704230400000000000000
    print(c == 126886932185884164103433389335161480802865516174545192198801894375214704230400000000000000)
    print()

    c, _ = count(100)
    print(c) # 0
    print(not c)
