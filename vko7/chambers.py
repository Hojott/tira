def count(r):
    rooms = 0
    dots_in_other_rooms = set()
    for i, row in enumerate(r):
        for j, dot in enumerate(row):
            if dot == '.':
                if find_room((i, j), dots_in_other_rooms, r):
                    rooms += 1

    return rooms

def find_room(coords: tuple, dots_in_other_rooms: set, r: list):
    """ count helper """
    dots_used = set()
    important_stuff = {
        "dots_used": dots_used,
        "dots_in_other_rooms": dots_in_other_rooms,
        "r": r
    }

    istrue = False
    if find_room_helper(coords, important_stuff):
        istrue = True

    for i in dots_used:
        dots_in_other_rooms.add(i)

    return istrue

def find_room_helper(coords, stuff: dict):
    stuff["dots_used"].add(coords)
    for next_coords in dots_around(coords):
        if stuff["r"][next_coords[0]][next_coords[1]] == '.':
            if next_coords in stuff["dots_in_other_rooms"]:
                return False

            if next_coords in stuff["dots_used"]:
                continue

            find_room_helper(next_coords, stuff)

    return True

def dots_around(coords):
    l = []
    l.append((coords[0], coords[1]-1))
    l.append((coords[0]-1, coords[1]))
    l.append((coords[0]+1, coords[1]))
    l.append((coords[0], coords[1]+1))
    return l

if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3

    r = ["##########",
    "#.#...#.##",
    "#..#...#.#",
    "###...#..#",
    "#.##...#.#",
    "##.......#",
    "#.##.....#",
    "#..#.#.#.#",
    "#..##.#.##",
    "##########"]
    print(count(r)) # 7
