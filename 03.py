import numpy as np

INPUT = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''.split()


def number_of_trees(INPUT):
    '''counts number of trees in slope (1, 3)'''
    # turn list of strings into np array
    INPUT = np.char.replace(INPUT, '.', '0')
    INPUT = np.char.replace(INPUT, '#', '1')

    INPUT = np.array([[number for number in line] for line in INPUT])
    INPUT = INPUT.astype(int)

    # get necessary width
    length, width = INPUT.shape
    necessary_width = length * 3 - 2
    repeats = int(np.ceil(necessary_width / width))
    INPUT = np.tile(INPUT, repeats)

    # count trees with slope (1, 3)
    result = sum([INPUT[i][i*3] for i in range(len(INPUT))])
    return result

assert(number_of_trees(INPUT) == 7)

with open('03.txt', 'r') as o:
    lines = o.read().splitlines()

print(number_of_trees(lines))


def number_of_trees_two(INPUT, slopes):
    '''counts number of trees for list of slopes
    return product of trees on the way'''
    # turn list of strings into np array
    INPUT = np.char.replace(INPUT, '.', '0')
    INPUT = np.char.replace(INPUT, '#', '1')

    INPUT = np.array([[number for number in line] for line in INPUT])
    INPUT = INPUT.astype(int)

    # get necessary width
    length, width = INPUT.shape

    trees = 1

    for slope in slopes:
        necessary_width = length * slope[1] - 2
        repeats = int(np.ceil(necessary_width / width))
        forrest = np.tile(INPUT, repeats)

        # count trees with slope 
        result = sum([forrest[i][int(i * slope[1] / slope[0])] for i in range(0, len(forrest), slope[0])])
        trees *= result

    return trees

slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

assert(number_of_trees_two(INPUT, slopes) == 336)

print(number_of_trees_two(lines, slopes))