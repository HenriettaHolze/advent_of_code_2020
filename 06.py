INPUT = '''abc

a
b
c

ab
ac

a
a
a
a

b'''.split('\n\n')

def count_any(groups):
    '''Count letters that appear in any of the lines'''
    count = 0
    for group in groups:
        # have to split and join to remove newline characters
        count += len(set(''.join(group.split())))
        print(set(group))
    return count

assert(count_any(INPUT) == 11)

with open('06.txt', 'r') as o:
    # split passports on blank lines
    groups = o.read().split('\n\n')

print(count_any(groups))



def count_all(groups):
    '''Count letters that appear in all lines'''
    # solved by finding intersection between list of sets
    count = 0

    for group in groups:
        # list of sets 
        lst = [set(person) for person in group.split()]
        # One-Liner to intersect a list of sets
        # single star 'unpacks' elemenst
        count += len(lst[0].intersection(*lst))

    return count

assert(count_all(INPUT) == 6)

print(count_all(groups))