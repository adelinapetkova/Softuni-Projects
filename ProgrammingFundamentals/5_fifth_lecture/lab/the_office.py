employees_happiness = [int(el) for el in input().split()]
factor = int(input())

list_happiness = [el * factor for el in employees_happiness]
average_happiness = sum(list_happiness) / len(list_happiness)
happy_employees = [el for el in list_happiness if el >= average_happiness]

if len(happy_employees) >= len(list_happiness) / 2:
    print(f'Score: {len(happy_employees)}/{len(list_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(happy_employees)}/{len(list_happiness)}. Employees are not happy!')
