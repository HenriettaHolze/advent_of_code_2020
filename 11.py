from copy import deepcopy

INPUT = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''.split()

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.

# strings are immutable and I want to change things on the go
# -> turn into list of lists of strings

def prep_input(INPUT):
    height = len(INPUT)
    width = len(INPUT[0])

    # padding
    INPUT = [['.'] + [char for char in line] + ['.']
            for line in INPUT]

    INPUT = [['.' for i in range(len(INPUT[0]))]] + INPUT + [['.' for i in range(len(INPUT[0]))]]

    return INPUT, width, height

def one_iteration(INPUT, width, height):
    next_pattern = deepcopy(INPUT)
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            # print(i, j)
            adjacent_seats = INPUT[i-1][j-1:j+2] + [INPUT[i][j-1]] + [INPUT[i][j+1]] + INPUT[i+1][j-1:j+2]
            if INPUT[i][j] == 'L':
                if '#' not in adjacent_seats:
                    next_pattern[i][j] = '#'
            if INPUT[i][j] == '#':
                if adjacent_seats.count('#') >= 4:
                    next_pattern[i][j] = 'L'

    return next_pattern


def find_seating(INPUT_raw):
    INPUT, width, height = prep_input(INPUT_raw)

    next_pattern = []
    while True:
        next_pattern = one_iteration(INPUT, width, height)
        if next_pattern == INPUT:
            break
        INPUT = deepcopy(next_pattern)

    return sum([i.count('#') for i in INPUT])

# assert(find_seating(INPUT) == 37)

with open('11.txt', 'r') as o:
    lines = o.read().splitlines()
    print(find_seating(lines))


# ======================================================
# part 2
# look into 8 directions 
# for each seat, create list which seats they can see as tuples (row, col)
# this never changes!


# INPUT, width, height = prep_input(INPUT)

def make_sight_dict(INPUT, width, height):
    sights = {}
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            if INPUT[i][j] == '.':
                continue
            print(i, j)
            sights[(i, j)] = []
            # right direction:
            for x in range(j + 1, width + 1):
                # print(i, x, INPUT[i][x])
                if INPUT[i][x] != '.':
                    sights[(i, j)].append((i, x))
                    break
            # bottom-right direction
            for x in range(1, min(width - j, height - i) + 1):
                # print(INPUT[i + x][j + x])
                if INPUT[i + x][j + x] != '.':
                    sights[(i, j)].append((i + x, j + x))
                    break
            # bottom direction
            for x in range(i + 1, height + 1):
                # print(x, j, INPUT[x][j])
                if INPUT[x][j] != '.':
                    sights[(i, j)].append((x, j))
                    break
            # bottom-left direction
            for x in range(1, min(j, height - i) + 1):
                # print(INPUT[i + x][j - x])
                if INPUT[i + x][j - x] != '.':
                    sights[(i, j)].append((i + x, j - x))
                    break
            # left direction
            for x in range(1, j):
                # print(INPUT[i][j - x])
                if INPUT[i][j - x] != '.':
                    sights[(i, j)].append((i, j - x))
                    break
            # top-left direction
            for x in range(1, min(j, i) + 1):
                # print(INPUT[i - x][j - x])
                if INPUT[i - x][j - x] != '.':
                    sights[(i, j)].append((i - x, j - x))
                    break
            # top direction
            for x in range(1, i):
                # print(INPUT[i - x][j])
                if INPUT[i - x][j] != '.':
                    sights[(i, j)].append((i - x, j))
                    break
            # top-right direction
            for x in range(1, min(width - j, i) + 1):
                # print(INPUT[i - x][j + x])
                if INPUT[i - x][j + x] != '.':
                    sights[(i, j)].append((i - x, j + x))
                    break
    return sights


def one_iteration_sight(INPUT, width, height, sights):
    next_pattern = deepcopy(INPUT)
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            if INPUT[i][j] == '.':
                continue
            # print(i, j)
            seats_in_sight = [INPUT[sight[0]][sight[1]]
                                for sight in sights[(i, j)]]
            if INPUT[i][j] == 'L':
                if '#' not in seats_in_sight:
                    next_pattern[i][j] = '#'
            if INPUT[i][j] == '#':
                if seats_in_sight.count('#') >= 5:
                    next_pattern[i][j] = 'L'
    return next_pattern


def find_seating2(INPUT_raw):
    INPUT, width, height = prep_input(INPUT_raw)
    sights = make_sight_dict(INPUT, width, height)

    next_pattern = []
    while True:
        next_pattern = one_iteration_sight(INPUT, width, height, sights)
        if next_pattern == INPUT:
            break
        INPUT = deepcopy(next_pattern)

    return sum([i.count('#') for i in INPUT])


print(find_seating2(lines))