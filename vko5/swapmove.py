class FuckYou(Exception):
    pass

def is_sorted(t):
    for i in range(1, len(t)):
        if t[i] < t[i-1]:
            return False
    return True

def solve(t):
    tc = t[:]
    moves = []

    def swap():
        hold = tc[1]
        tc[1] = tc[0]
        tc[0] = hold
        moves.append("SWAP")

    def move():
        tc.append(tc[0])
        tc.pop(0)
        moves.append("MOVE")

    while not is_sorted(tc):
        #print(tc)

        if tc[1] > tc[0]:
            swap()
        elif tc[-1] > tc[0]:
            swap()
        elif tc[0] > len(tc)//2:
            move()
        else:
            swap()

        if t == tc or len(moves) > len(tc)**3:
            raise FuckYou()

    return moves

if __name__ == "__main__":
    print(solve([1, 2])) # esim. []
    print(solve([2, 1])) # esim. [SWAP]
    print(solve([1, 3, 2])) # esim. [SWAP, MOVE]
    print(solve([3, 2, 1])) # esim. [MOVE, SWAP]
    print(solve([2, 3, 4, 1])) # esim. [MOVE, MOVE, MOVE]
    print(solve([1, 5, 2, 10, 4, 8, 7, 3, 6, 9]))
