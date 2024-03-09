def count(r):
    places_been = set()

    for i, row in enumerate(r):
        for j, dot in enumerate(row):
            if dot == 'A':
                coords = (i, j)

    places_been.add(coords)
    layers = [[coords]]

    while 1:
        width = len(layers)
        layer = []

        for coords in layers[width-1]:
            for new_coords in dots_around(coords):
                if new_coords in places_been:
                    continue

                places_been.add(new_coords)
                new_dot = r[new_coords[0]][new_coords[1]]

                if new_dot == '.':
                    layer.append(new_coords)
                
                if new_dot == 'B':
                    return width
                
        if not layer:
            return -1

        layers.append(layer)        

def dots_around(coords):
    l = []  # noqa: E741
    l.append((coords[0]-1, coords[1]))
    l.append((coords[0], coords[1]-1))
    l.append((coords[0], coords[1]+1))
    l.append((coords[0]+1, coords[1]))
    return l

if __name__ == "__main__":
    """
    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "#.##...#",
         "#...B#.#",
         "########"]
    print(count(r)) # 7

    r = ["##########",
    "#........#",
    "#........#",
    "#........#",
    "#........#",
    "###.....##",
    "##.......#",
    "#.#...#..#",
    "##.B...A.#",
    "##########"]
    print(count(r)) # 4
    """

    r = ["####################",
    "#.#....#...........#",
    "#..................#",
    "##.....#...........#",
    "#..................#",
    "#..................#",
    "#..................#",
    "#..................#",
    "#..................#",
    "#.......A..........#",
    "#..................#",
    "#...#..............#",
    "#................B.#",
    "#..................#",
    "#..................#",
    "#..................#",
    "#..............#...#",
    "#..................#",
    "#..................#",
    "####################"]

    print(count(r)) # 12
