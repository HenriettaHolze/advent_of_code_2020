import regex as re

INPUT = '1 + 2 * 3 + 4 * 5 + 6'
INPUT = '1 + (2 * 3) + (4 * (5 + 6))'
INPUT = '2 * 3 + (4 * 5)'
INPUT = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
INPUT = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
INPUT = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'


# resolve from left to right
def solve_ltr(INPUT):
    regex = r'^([0-9]+ . [0-9]+)'
    pattern = re.compile(regex)
    while re.search(pattern, INPUT):
        m = re.search(pattern, INPUT)
        result = eval(m[0])
        INPUT = INPUT[:m.span()[0]] + str(result) + INPUT[m.span()[1]:]

    return INPUT

def solve_brackets(INPUT):
    # non greedy match
    regex = r'\(([^\()]*?)\)'
    pattern = re.compile(regex)

    while re.search(pattern, INPUT):
        # find position of pattern, evaluate pattern and replace it in string
        matches_spans = [m.span() for m in re.finditer(pattern, INPUT)]
        matches_groups = re.findall(pattern, INPUT)

        matches = list(zip(matches_spans, matches_groups))

        matches.reverse()

        # go reverse through matches so indexing into string works
        for m in matches:
            result = solve_ltr(m[1])
            INPUT = INPUT[:m[0][0]] + str(result) + INPUT[m[0][1]:]
            # print(INPUT)

    INPUT = solve_ltr(INPUT)

    return int(INPUT)



# print(solve_brackets(INPUT))


# resolve with inverted precedence
def solve_plus(INPUT):
    regex = r'([0-9]+ \+ [0-9]+)'
    pattern = re.compile(regex)
    while re.search(pattern, INPUT):
        m = re.search(pattern, INPUT)
        result = eval(m[0])
        INPUT = INPUT[:m.span()[0]] + str(result) + INPUT[m.span()[1]:]
        # print(INPUT)

    return INPUT

def solve_mult(INPUT):
    regex = r'([0-9]+ \* [0-9]+)'
    pattern = re.compile(regex)
    while re.search(pattern, INPUT):
        m = re.search(pattern, INPUT)
        result = eval(m[0])
        INPUT = INPUT[:m.span()[0]] + str(result) + INPUT[m.span()[1]:]
        # print(INPUT)

    return INPUT

def solve_inv(INPUT):
    regex = r'^([0-9]+ . [0-9]+)'
    pattern = re.compile(regex)
    while re.search(pattern, INPUT):
        INPUT = solve_plus(INPUT)
        INPUT = solve_mult(INPUT)
        # print(INPUT)

    return INPUT




def solve_brackets_inv(INPUT):
    # non greedy match
    regex = r'\(([^\()]*?)\)'
    pattern = re.compile(regex)

    while re.search(pattern, INPUT):
        # find position of pattern, evaluate pattern and replace it in string
        matches_spans = [m.span() for m in re.finditer(pattern, INPUT)]
        matches_groups = re.findall(pattern, INPUT)

        matches = list(zip(matches_spans, matches_groups))

        matches.reverse()

        # go reverse through matches so indexing into string works
        for m in matches:
            result = solve_inv(m[1])
            INPUT = INPUT[:m[0][0]] + str(result) + INPUT[m[0][1]:]
            # print(INPUT)

    INPUT = solve_inv(INPUT)

    return int(INPUT)

# print(solve_brackets_inv(INPUT))


with open('18.txt', 'r') as o:
    lines = o.read().splitlines()
    print(sum([solve_brackets(line) for line in lines]))
    print(sum([solve_brackets_inv(line) for line in lines]))
