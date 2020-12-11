INPUT = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''.split('\n')

INPUT = [int(number) for number in INPUT]

def find_invalid_number(INPUT, preambel_size):
    # for example input, preambel is only 5 numbers long
    for i in range(preambel_size, len(INPUT)):
        # make 2 sets with the preambel and the subtraction
        preambel = {INPUT[i - j - 1] for j in range(preambel_size)}
        differences = {INPUT[i] - number for number in preambel}
        # if the number is the sum of 2 numbers in the preambel, the numbers will appear in both sets
        if len(preambel - differences) >= preambel_size:
            return INPUT[i], i
        

assert(find_invalid_number(INPUT, 5)[0] == 127)


with open('09.txt', 'r') as o:
    numbers = [int(number.strip()) for number in o.readlines()]
    invalid_number, position = find_invalid_number(numbers, 25)


print(invalid_number, position)

invalid_number_INPUT = 127
position_INPUT = find_invalid_number(INPUT, 5)[1]

def find_range(INPUT, position, invalid_number):
    for i in range(len(INPUT)):
        if i == position:
            continue

        summand = 0
        j = i
        contiguous_numbers = []
        while summand < invalid_number:
            summand += INPUT[j]
            contiguous_numbers.append(INPUT[j])
            j += 1
        
        if summand == invalid_number:
            return max(contiguous_numbers) + min(contiguous_numbers)


assert(find_range(INPUT, position_INPUT, invalid_number_INPUT) == 62)

print(find_range(numbers, position, invalid_number))

