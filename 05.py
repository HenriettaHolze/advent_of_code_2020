from math import floor, ceil
INPUT = 'FBFBBFFRLR'

def find_seat(pattern):
    '''Find assigned seat and return seat ID'''

    row_spec, col_spec = pattern[:-3], pattern[-3:]

    # find row
    row_lower = 0
    row_upper = 127
    for i, letter in enumerate(row_spec):
        if letter == 'B':
            row_lower += ceil((row_upper - row_lower) / 2)
        else:
            row_upper -= ceil((row_upper - row_lower) / 2)

    assert(row_lower == row_upper)

    row = row_lower

    # find column
    col_lower = 0
    col_upper = 7
    for i, letter in enumerate(col_spec):
        if letter == 'R':
            col_lower += ceil((col_upper - col_lower) / 2)
        else:
            col_upper -= ceil((col_upper - col_lower) / 2)

    assert(col_lower == col_upper)

    col = col_lower

    seat_id = row * 8 + col
    return seat_id


assert(find_seat(INPUT) == 357)

with open('05.txt', 'r') as o:
    boarding_passes = o.read().splitlines()
    print('highest seat ID:', max([find_seat(boarding_pass) for boarding_pass in boarding_passes]))

# -----------------------------------------------------------------
# Part 2

taken_seats = set([find_seat(boarding_pass) for boarding_pass in boarding_passes])

possible_seats = {
    i * 8 + j
    for i in range(128)
    for j in range(8)
}

available_seats = possible_seats - taken_seats

for seat in available_seats:
    if seat - 1 not in available_seats and seat + 1 not in available_seats:
        print('your seat ID:', seat)
