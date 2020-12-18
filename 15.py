starting_numbers = [0, 3, 6]
starting_numbers = [19,20,14,0,9,1]

turn = 0

spoken_numbers = {}

all_numbers = []

for number in starting_numbers:
    turn += 1
    if number not in spoken_numbers:
        spoken_numbers[number] = []
    spoken_numbers[number].append(turn)


while turn != 30000000:
    turn += 1
    if len(spoken_numbers[number]) == 1:
        number = 0
    else:
        number = spoken_numbers[number][-1] - spoken_numbers[number][-2]
    if number not in spoken_numbers:
        spoken_numbers[number] = []
    spoken_numbers[number].append(turn)
    if turn % 10000 == 0:
        print(turn)
    # all_numbers.append(number)


print(turn, number)