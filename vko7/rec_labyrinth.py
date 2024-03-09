import asyncio
 
def count(r):
    moves_taken = dict()
    shortest = []
    coords = (0, 0)
    for i, row in enumerate(r):
        for j, dot in enumerate(row):
            if dot == 'A':
                coords = (i, j)
 
    asyncio.run(count_helper(coords, 0, moves_taken, shortest, r))
 
    if not shortest:
        return -1
    return shortest[0]
 
async def count_helper(coords, i, moves_taken, shortest, r):
    task_list = set()
 
    for next_coords in dots_around(coords):
        next_dot = r[next_coords[0]][next_coords[1]]
 
        if (coords, next_coords) in moves_taken and i+1 > moves_taken[(coords, next_coords)]:
            continue
        moves_taken[(coords, next_coords)] = i+1
 
        if next_dot == 'B':
            #print(coords, "->", next_coords)
            #print(route_lengths)
            shortest.append(i+1)
            if len(shortest) > 2:
                shortest.remove(max(shortest))
 
        if next_dot == '.':
            #print(coords, "->", next_coords)
            if shortest and i+1 > shortest[0]:
                return
            t = asyncio.create_task(count_helper(next_coords, i+1, moves_taken, shortest, r))
            task_list.add(t)
            #t.add_done_callback(task_list.discard)
    
    for t in task_list:
        await asyncio.shield(t)
 
 
def dots_around(coords):
    l = []
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
    print(count(r))
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

    print(count(r))