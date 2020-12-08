INPUT = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.split('\n')


def find_loop(INPUT):
    '''finds the value of the accumulator before the game enters the second loop'''
    position = 0
    accumulator = 0
    visited_positions = []

    while position not in visited_positions:
        instructions = INPUT[position].strip().split()
        # print(position, instructions)
        visited_positions.append(position)
        if instructions[0] == 'nop':
            position += 1
            continue
        elif instructions[0] == 'jmp':
            position += int(instructions[1])
            continue
        else: 
            accumulator += int(instructions[1])
            position += 1

    return accumulator
    

assert(find_loop(INPUT) == 5)




def find_end(INPUT):
    '''finds the value of the accumulator after the game ends'''
    target_position = len(INPUT)
    position = 0
    accumulator = 0
    visited_positions = []

    while position not in visited_positions and position != target_position:
        instructions = INPUT[position].strip().split()
        # print(position, instructions)
        visited_positions.append(position)
        if instructions[0] == 'nop':
            position += 1
            continue
        elif instructions[0] == 'jmp':
            position += int(instructions[1])
            continue
        else: 
            accumulator += int(instructions[1])
            position += 1

    return accumulator, position == target_position


def bruteforce_instructions(INPUT):
    '''Change all jmp to nop (one at a time) to find corrupted position 
    in instructions that leads to infinite loop'''
    for i in range(len(INPUT)):
        if INPUT[i].startswith('jmp'):
            changed_input = INPUT.copy()
            changed_input[i] = 'nop ' + INPUT[i][4:]
            # print(i, INPUT[i], changed_input[i])
            result = find_end(changed_input)
            # quit once end was found
            if result[1]:
                return result[0]


assert(bruteforce_instructions(INPUT) == 8)


with open('08.txt', 'r') as o:
    lines = o.readlines()
    print(find_loop(lines))
    print(bruteforce_instructions(lines))