n = int(input())

students = {}

for _ in range(n):
    name, grade = input().split()
    grade = float(grade)
    if name not in students:
        students[name] = []
    students[name].append(grade)

for key, value in students.items():
    average = sum(value) / len(value)
    value = [str(f'{grade:.2f}') for grade in value]
    print(f'{key} -> {" ".join(value)} (avg: {average:.2f})')
