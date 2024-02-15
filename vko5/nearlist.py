class NearList:
    def __init__(s, t):
        s.t = sorted(list(set(t)))

    def find(s, x):
        """ using binary search """
        left = 0
        right = len(s.t)
        mid = right // 2
        prev = 0
        #print(s.t, mid)

        while right-left > 1:
            
            if s.t[mid] == x:
                return x

            if s.t[mid] > x:
                right = mid
            elif s.t[mid] < x:
                left = mid

            prev = s.t[mid]
            mid = left + (right-left) // 2
            #print(mid)
            
        if mid:
            if abs(x - s.t[mid-1]) <= abs(x - s.t[mid]):
                return s.t[mid-1]

        try:
            if abs(x - s.t[mid]) <= abs(x - s.t[mid+1]):
                return s.t[mid]
        except IndexError:
            return s.t[mid]
        
        return s.t[mid+1]


if __name__ == "__main__":
    n = NearList([3, 6, 1, 3, 9, 8])
    """print(n.find(1)) # 1
    print(n.find(2)) # 1
    print(n.find(3)) # 3
    print(n.find(4)) # 3
    print(n.find(5)) # 6
    print(n.find(6)) # 6
    print(n.find(7)) # 6
    print(n.find(8)) # 8
    print(n.find(9)) # 9
    
    print()
    """
    n = NearList([15, 32, 72, 29, 29, 80, 41])
    print(n.find(31))

