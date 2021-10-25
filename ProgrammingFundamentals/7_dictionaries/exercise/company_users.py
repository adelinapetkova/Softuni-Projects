command = input()
company_employees = {}

while not command == 'End':
    company, employee_id = command.split(' -> ')
    if company not in company_employees:
        company_employees[company] = []
    if employee_id not in company_employees[company]:
        company_employees[company].append(employee_id)
    command = input()

a = dict(sorted(company_employees.items(), key=lambda x: x[0]))

for key, value in a.items():
    print(f'{key}')
    for em_id in value:
        print(f'-- {em_id}')