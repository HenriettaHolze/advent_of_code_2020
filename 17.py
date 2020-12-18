import numpy as np
from copy import deepcopy


INPUT = '''.#.
..#
###'''.split()


# day 11
# before ever iteration, pad 
def prep_input(INPUT):

    # turn into numpy array
    INPUT = np.char.replace(INPUT, '.', '0')
    INPUT = np.char.replace(INPUT, '#', '1')

    INPUT = np.array([[number for number in line] for line in INPUT])
    INPUT = INPUT.astype(int)

    # get necessary width
    height, width = INPUT.shape

    # introduce 3rd dimension
    INPUT = INPUT.reshape(height, width, 1)

    INPUT = np.pad(INPUT, 1)

    return INPUT


def get_neighbors(INPUT, x, y, z):
    neighbors = INPUT[x-1:x+2, y-1:y+2, z-1:z+2].flatten()
    # delete central element
    neighbors = np.delete(neighbors, 13)
    return neighbors


def one_iteration(INPUT):
    height, width, depth = INPUT.shape
    # padding
    INPUT = np.pad(INPUT, 1)

    next_pattern = deepcopy(INPUT)
    # the 1/+1 is for the padding and will not be checked 
    for x in range(1, height + 1):
        for y in range(1, width + 1):
            for z in range(1, depth + 1):
                neighbors = get_neighbors(INPUT, x, y, z)

                # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
                if INPUT[x, y, z] == 1:
                    if not 2 <= neighbors.sum() <= 3:
                        next_pattern[x, y, z] = 0
                # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
                if INPUT[x, y, z] == 0:
                    if neighbors.sum() == 3:
                        next_pattern[x, y, z] = 1

    return next_pattern

def six_iterations(INPUT):
    INPUT = prep_input(INPUT)
    for i in range(6):
        
        next_pattern = one_iteration(INPUT)
        INPUT = deepcopy(next_pattern)
    return INPUT.sum()

assert(six_iterations(INPUT) == 112)


# -----------------------------------------------------------------------------
def prep_input_4d(INPUT):

    # turn into numpy array
    INPUT = np.char.replace(INPUT, '.', '0')
    INPUT = np.char.replace(INPUT, '#', '1')

    INPUT = np.array([[number for number in line] for line in INPUT])
    INPUT = INPUT.astype(int)

    # get necessary width
    height, width = INPUT.shape

    # introduce 3rd and 4th dimension
    INPUT = INPUT.reshape(height, width, 1, 1)

    INPUT = np.pad(INPUT, 1)
    
    return INPUT


def get_neighbors_4d(INPUT, x, y, z, w):
    neighbors = INPUT[x-1:x+2, y-1:y+2, z-1:z+2, w-1:w+2].flatten()
    # delete central element
    neighbors = np.delete(neighbors, 40)
    return neighbors


def one_iteration_4d(INPUT):
    height, width, depth, fourth = INPUT.shape
    # padding
    INPUT = np.pad(INPUT, 1)

    next_pattern = deepcopy(INPUT)
    for x in range(1, height + 1):
        for y in range(1, width + 1):
            for z in range(1, depth + 1):
                for w in range(1, fourth + 1):
                    neighbors = get_neighbors_4d(INPUT, x, y, z, w)

                    # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
                    if INPUT[x, y, z, w] == 1:
                        if not 2 <= neighbors.sum() <= 3:
                            next_pattern[x, y, z, w] = 0
                    # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
                    if INPUT[x, y, z, w] == 0:
                        if neighbors.sum() == 3:
                            next_pattern[x, y, z, w] = 1

    return next_pattern

def six_iterations_4d(INPUT):
    INPUT = prep_input_4d(INPUT)
    for i in range(6):
        
        next_pattern = one_iteration_4d(INPUT)
        INPUT = deepcopy(next_pattern)

    return INPUT.sum()


assert(six_iterations_4d(INPUT) == 848)


with open('17.txt', 'r') as o:
    lines = o.read().splitlines()
    print(six_iterations(lines))
    print(six_iterations_4d(lines))
