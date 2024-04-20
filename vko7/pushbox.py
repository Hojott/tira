def count(r):
    """ using widthsearch """
    pcoords, bcoords, wcoords = start_coords(r)

    turns = [
      # set((pcoords, bcoords))
      # set((pcoords, bcoords), (pcoords, bcoords), ...)
      # ...
    ]
    turns.append(set())
    turns[0].add( (pcoords, bcoords) )

    all_moves = set()

    i = 0
    while 1: #TODO
        turns.append(set())
        no_new_coords = True

        i += 1
        for (pcoords, bcoords) in turns[i-1]:

            for new_pcoords in spots_around(pcoords):
                new_pchar = r[new_pcoords[0]][new_pcoords[1]]

                if new_pchar == '#':
                    continue

                if new_pcoords == bcoords:
                    new_bcoords = (
                        bcoords[0]+(new_pcoords[0]-pcoords[0]),
                        bcoords[1]+(new_pcoords[1]-pcoords[1])
                    )

                    new_bchar = r[new_bcoords[0]][new_bcoords[1]]
                
                    if new_bchar == 'Y':
                        return i
                    if new_bchar == '#':
                        continue

                else:
                    new_bcoords = bcoords
            
                if (new_pcoords, new_bcoords) not in all_moves:
                    no_new_coords = False
                    turns[i].add((new_pcoords, new_bcoords))
                all_moves.add((new_pcoords, new_bcoords))
            
        if no_new_coords:
            return -1


def start_coords(r) -> tuple[list[int, int], list[int, int], list[int, int]]:
    for i, row in enumerate(r):
        for j, char in enumerate(row):
            if char == 'X':
                pcoords = (i, j)
            if char == 'B':
                bcoords = (i, j)
            if char == 'Y':
                wcoords = (i, j)

    return pcoords, bcoords, wcoords

def spots_around(coords) -> list:
    around = []
    around.append((coords[0]-1, coords[1]))
    around.append((coords[0]+1, coords[1]))
    around.append((coords[0], coords[1]-1))
    around.append((coords[0], coords[1]+1))
    return around


if __name__ == "__main__":
    r = ["########",
         "#......#",
         "#.#.Y#.#",
         "#.#B.#.#",
         "#..X.#.#",
         "#.#..#.#",
         "########"]
    print(count(r)) # 18
    
    r= ["####################",
    "#..#..#..#.........#",
    "#.#.....#..#####...#",
    "#.......#.......#..#",
    "#..#..#....#.#...#.#",
    "#..#.....#.#..#..#.#",
    "#....#....#...#..#.#",
    "#....#......#..#.#.#",
    "#.....#.##.......#.#",
    "#..#..........#.#..#",
    "##...#.#####.#...#.#",
    "#............#.....#",
    "#..#..........#....#",
    "#.#.....#......#.#.#",
    "#..#....#.......X#.#",
    "#..#....#...#..#.#.#",
    "#.Y..###...#....#..#",
    "#.........#....B...#",
    "#..#...#.#....#....#",
    "####################"]
    print(count(r)) # 63
