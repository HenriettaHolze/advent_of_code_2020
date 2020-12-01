# --- Day 1: Report Repair ---

with open('1.txt', 'r') as o:
    expenses = [int(expense) for expense in o.read().splitlines()]

# print(expenses)

found = False
for i, expense in enumerate(expenses):
    for j, second_expense in enumerate(expenses[i + 1:]):
        if expense + second_expense == 2020:
            print('found')
            found = True
            break 
    if found:
        break

print('product is:', expense * second_expense)



# --- Part Two ---

found = False
for i, expense in enumerate(expenses):
    for j, second_expense in enumerate(expenses[i + 1:]):
        if expense + second_expense >= 2020:
            continue
        for k, third_expense in enumerate(expenses[i + 1:]):
            if expense + second_expense + third_expense == 2020:
                print('found')
                found = True
                break 
        if found:
            break
    if found:
        break

print('product is:', expense * second_expense * third_expense)
