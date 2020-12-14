INPUT = '''F10
N3
F7
R90
F11'''.split()


def turn_left(direction):
    if direction == 'E':
        direction = 'N'
    elif direction == 'N':
        direction = 'W'
    elif direction == 'W':
        direction = 'S'
    elif direction == 'S':
        direction = 'E'

    return direction


def turn_right(direction):
    if direction == 'E':
        direction = 'S'
    elif direction == 'N':
        direction = 'E'
    elif direction == 'W':
        direction = 'N'
    elif direction == 'S':
        direction = 'W'

    return direction


def follow_instructions(INPUT):
    direction = 'E'

    movements = {'E': 0, 'N': 0, 'W': 0, 'S': 0}

    for command in INPUT:
        if command[0] == 'R':
            for i in range(int(int(command[1:]) / 90)):
                direction = turn_right(direction)
        elif command[0] == 'L':
            for i in range(int(int(command[1:]) / 90)):
                direction = turn_left(direction)
        elif command[0] == 'F':
            movements[direction] += int(command[1:])
        else:
            movements[command[0]] += int(command[1:])

    manhattan_distance = abs(movements['E'] - movements['W']) + abs(movements['S'] - movements['N'])
    return manhattan_distance

assert(follow_instructions(INPUT) == 25)

with open('12.txt', 'r') as o:
    lines = o.read().splitlines()
    print(follow_instructions(lines))