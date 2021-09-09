command=input()
courses={}

while not command=='end':
    course, name=command.split(' : ')
    if course not in courses:
        courses[course]=[]
    courses[course].append(name)
    command=input()

a=dict(sorted(courses.items(), key=lambda x: -len(x[1])))

for key, value in a.items():
    print(f'{key}: {len(value)}')
    b=list(sorted(value))
    for student in b:
        print(f'-- {student}')