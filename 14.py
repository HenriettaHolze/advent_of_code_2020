import re

def to_bits(myint):
    '''turns integer into 36 bit string'''
    bit = "{0:b}".format(myint).zfill(36)
    return bit

def mask_bits(mask, string):
    '''masks bit string'''
    new_string = ''
    for i in range(len(mask)):
        if mask[i] != 'X':
            new_string += mask[i]
        else: 
            new_string += string[i]

    return new_string


INPUT = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''.split('\n')

INPUT = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''.split('\n')


def decode(INPUT):

    mem = {}

    pattern = re.compile(r'\[([0-9]*)\] = ([0-9]*)')

    for line in INPUT:
        if line.startswith('mask'):
            mask = line.split()[-1]
            continue
        groups = re.search(pattern, line).groups()
        mem[groups[0]] = int(mask_bits(mask, to_bits(int(groups[1]))), 2)

    return sum(mem.values())


# string = to_bits(int(position))

def mask_position(mask, string):
    new_string = ''
    for i in range(len(mask)):
        if mask[i] == '1':
            new_string += '1'
        elif mask[i] == 'X':
            new_string += '0'
        else: 
            new_string += string[i]

    possible_positions = [new_string]
    for i in range(len(mask)):
        if mask[i] == 'X':
            add_pos = []
            for pos in possible_positions:
                add_pos.append(pos[:i] + '1' + pos[i+1:])
            possible_positions.extend(add_pos)

    return [int(pos, 2) for pos in possible_positions]


def decode_pos(INPUT):

    mem = {}

    pattern = re.compile(r'\[([0-9]*)\] = ([0-9]*)')

    for line in INPUT:
        if line.startswith('mask'):
            mask = line.split()[-1]
            continue
        groups = re.search(pattern, line).groups()

        possible_positions = mask_position(mask, to_bits(int(groups[0])))

        for pos in possible_positions:
            mem[pos] = int(groups[1])

    return sum(mem.values())



with open('14.txt', 'r') as o:
    lines = o.read().splitlines()
    print(decode(lines))
    print(decode_pos(lines))
    