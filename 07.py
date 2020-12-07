INPUT = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''.split('\n')

# make dict
# bag contains [bag, bag]
# {bag: [bag, bag]}
# python dicts are basically pointers


def make_bag_dict(INPUT):

    bag_dict = {}

    for line in INPUT:
        bag = ' '.join(line.split()[:2])
        contents = ' '.join(line.split()[4:])[:-1].split(', ')
        if contents == ['no other bags']:
            bag_dict[bag] = []
            continue
        bag_dict[bag] = [' '.join(content.split()[1:3]) for content in contents]

    return bag_dict


def find_bag_number(bag_dict):
    bag_num = 0

    for mybag in bag_dict.keys():

        visited_bags = []

        found = False

        # if I don't copy, this will empty the whole bag_dict
        mycontents = bag_dict[mybag].copy()
        if 'shiny gold' in mycontents:
            bag_num += 1
            continue

        while mycontents != []:
            my_inner_bag = mycontents.pop()
            visited_bags.append(my_inner_bag)

            if my_inner_bag == 'shiny gold':
                found = True
                break
            if not bag_dict[my_inner_bag] == []:
                for content in bag_dict[my_inner_bag]:
                    if content not in visited_bags:
                        mycontents.append(content)

        if found: 
            bag_num += 1

    return bag_num


assert(find_bag_number(make_bag_dict(INPUT)) == 4)

with open('07.txt', 'r') as o:
    lines = o.read().splitlines()

bag_dict = make_bag_dict(lines)
print(find_bag_number(bag_dict))


# --------------------------------------------------------------------------
# part 2


INPUT2 = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''.split('\n')


def make_bag_dict_extended(INPUT):

    bag_dict = {}

    for line in INPUT:
        bag = ' '.join(line.split()[:2])
        contents = ' '.join(line.split()[4:])[:-1].split(', ')
        if contents == ['no other bags']:
            bag_dict[bag] = []
            continue

        mylist = []
        for content in contents:
            for i in range(int(content.split()[0])):
                mylist.append(' '.join(content.split()[1:3]))

        bag_dict[bag] = mylist

    return bag_dict


def get_content(bag, bag_dict, counter):
    if bag_dict[bag] == []:
        return counter
    else:
        for bag in bag_dict[bag]:
            counter += 1
            counter = get_content(bag, bag_dict, counter)
        return counter


bag_dict_extended_INPUT2 = make_bag_dict_extended(INPUT2)
assert(get_content(bag='shiny gold', bag_dict=bag_dict_extended_INPUT2, counter=0) == 126)

bag_dict_extended_INPUT = make_bag_dict_extended(INPUT)
assert(get_content(bag='shiny gold', bag_dict=bag_dict_extended_INPUT, counter=0) == 32)

bag_dict_extended = make_bag_dict_extended(lines)
print(get_content(bag='shiny gold', bag_dict=bag_dict_extended, counter=0))
