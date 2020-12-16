INPUT = '''939
7,13,x,x,59,x,31,19'''.split()

def find_next_bus(INPUT):
    timestamp = int(INPUT[0])
    lines = INPUT[1].split(',')

    while 'x' in lines:
        lines.remove('x')

    lines_waiting_time = {
        line: timestamp // int(line) * int(line) + int(line) - timestamp
        for line in lines
    }
    return int(min(lines_waiting_time, key=lines_waiting_time.get)) * min(lines_waiting_time.values())

assert(find_next_bus(INPUT) == 295)

with open('13.txt', 'r') as o:
    notes = o.read().splitlines()
    print(find_next_bus(notes))