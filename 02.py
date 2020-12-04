import re

INPUT = ['1-3 a: abcde',
         '1-3 b: cdefg',
         '2-9 c: ccccccccc']

# create regex pattern that captures the numbers and letters and password
regex = '([0-9]*)-([0-9]*) ([a-z]): (.*)$'
pattern = re.compile(regex)


def check_password(lines):
    '''checks if passwords in a list are valid,
    returns number of valid passwords'''
    valid_passwords = 0
    for line in lines: 
        m = re.match(pattern, line)

        password = m.groups()[3]
        letter = m.groups()[2]
        lower = int(m.groups()[0])
        upper = int(m.groups()[1])

        if lower <= password.count(letter) <= upper:
            valid_passwords += 1

    return valid_passwords


assert(check_password(INPUT) == 2)

with open('02.txt', 'r') as o:
    lines = o.read().splitlines()

result = check_password(lines)
print(result)


def check_password_two(lines):
    '''checks if passwords in a list are valid,
    returns number of valid passwords'''
    valid_passwords = 0
    for line in lines: 
        m = re.match(pattern, line)

        password = m.groups()[3]
        letter = m.groups()[2]
        first = int(m.groups()[0])
        second = int(m.groups()[1])

        if (password[first - 1] == letter) ^ (password[second - 1] == letter):
            valid_passwords += 1

    return valid_passwords


assert(check_password_two(INPUT) == 1)

result = check_password_two(lines)
print(result)
