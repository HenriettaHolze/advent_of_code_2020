INPUT = '''16
10
15
5
1
11
7
19
6
12
4'''.split('\n')

INPUT2 = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''.split('\n')

INPUT = [int(number) for number in INPUT]


def find_differences(INPUT):
    INPUT = [int(number) for number in INPUT]
    
    INPUT = sorted(INPUT)

    diff1 = 0
    diff3 = 0

    differences = 0
    for i, number in enumerate(INPUT):
        if i == 0:
            if INPUT[i] == 1:
                diff1 += 1
            elif INPUT[i] == 3:
                diff3 += 1
            differences = INPUT[i]
        else: 
            if INPUT[i] - INPUT[i - 1] == 1:
                diff1 += 1
            elif INPUT[i] - INPUT[i - 1] == 3:
                diff3 += 1

            differences += INPUT[i] - INPUT[i - 1]

    differences += 3
    diff3 += 1

    return differences, diff1 * diff3


print(find_differences(INPUT))
print(find_differences(INPUT2))

with open('10.txt', 'r') as o:
    numbers = [int(number.strip()) for number in o.readlines()]

print(find_differences(numbers))




# for every number, find number of adapters it can connect to, then use combinatorics 
# or make class of adapter and points to 
# make dict of adapters, each pointing to where it can be connected to 

def make_path_dict(INPUT):
    INPUT = [int(number) for number in INPUT]

    INPUT = sorted(INPUT)

    INPUT = INPUT + [max(INPUT) + 3]
    INPUT = [0] + INPUT

    connections = {}
    for i, number in enumerate(INPUT):
        # print(i, number)
        connections[number] = []
        j = 1
        while i + j < len(INPUT) and INPUT[i + j] - number <= 3:
            # print('can connect to', INPUT[i + j])
            connections[number].append(INPUT[i + j])
            j += 1

    return connections

path_dict = make_path_dict(INPUT2)
path_dict = make_path_dict(numbers)

print(path_dict)


# this is a recursive solution but it takes >30 minutes
def find_paths(number, path_dict, counter, end):
    if path_dict[number] == [end]:
        # increment counter every time you finished a path
        counter += 1
        # print('found end', counter)
        return counter 
    else: 
        for number in path_dict[number]:
            counter = find_paths(number, path_dict, counter, end)
        return counter


# print(find_paths(0, path_dict, 0, 52))


# recursive solution takes too long 
# go from back to beginning, 
# find all sup-paths from number to end
# dict {number: number of paths}
# if number in dict: 

# find the nodes that are only in one of the dicts -> they have to be passed 

from collections import Counter
mynumbers = []
[mynumbers.extend(i) for i in path_dict.values()]

mycounts = Counter(mynumbers)

breakpoints = []
for i, number in enumerate(mycounts):
    if mycounts[number] == 1:
        print(len([i for i in list(path_dict.values()) if number in i][0]))
        if len([i for i in list(path_dict.values()) if number in i][0]) == 1:
            breakpoints.append(number)

breakpoints = [0] + breakpoints
print(breakpoints)


all_paths = 1
for i, bp in enumerate(breakpoints):
    if i == len(breakpoints) - 1:
        break
    print(bp, breakpoints[i + 1])
    all_paths *= find_paths(bp, path_dict, 0, breakpoints[i + 1])

print(all_paths)
