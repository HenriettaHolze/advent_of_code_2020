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


def equal_out(waypoint):
    if waypoint['S'] > waypoint['N']:
        waypoint['S'] -= waypoint['N']
        waypoint['N'] = 0
    elif waypoint['N'] > waypoint['S']:
        waypoint['N'] -= waypoint['S']
        waypoint['S'] = 0
    if waypoint['E'] > waypoint['W']:
        waypoint['E'] -= waypoint['W']
        waypoint['W'] = 0
    elif waypoint['W'] > waypoint['E']:
        waypoint['W'] -= waypoint['E']
        waypoint['E'] = 0

    return waypoint


def waypoint_instructions(INPUT):
    # The waypoint starts 10 units east and 1 unit north relative to the ship
    waypoint = {'E': 10, 'N': 1, 'W': 0, 'S': 0}

    movements = {'E': 0, 'N': 0, 'W': 0, 'S': 0}

    for command in INPUT:
        if command[0] == 'F':
            for direction, steps in waypoint.items():
                movements[direction] += steps * int(command[1:])
        elif command[0] == 'L':
            for i in range(int(int(command[1:]) / 90)):
                waypoint['N'], waypoint['W'], waypoint['S'], waypoint['E'] = waypoint['E'], waypoint['N'], waypoint['W'], waypoint['S']
        elif command[0] == 'R':
            for i in range(int(int(command[1:]) / 90)):
                # E 10, N 4 -> S 10, E 4
                waypoint['W'], waypoint['S'], waypoint['E'], waypoint['N'] = waypoint['S'], waypoint['E'], waypoint['N'], waypoint['W']
        else:
            waypoint[command[0]] += int(command[1:])
            
        # not really necessary
        # waypoint = equal_out(waypoint)
        # movements = equal_out(movements)
        
        # print(waypoint, movements)

    manhattan_distance = abs(movements['E'] - movements['W']) + abs(movements['S'] - movements['N'])
    return manhattan_distance

assert(waypoint_instructions(INPUT) == 286)

print(waypoint_instructions(lines))