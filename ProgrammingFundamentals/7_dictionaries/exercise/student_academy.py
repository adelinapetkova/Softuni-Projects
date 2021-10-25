n = int(input())
students = {}

for _ in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = grade
    else:
        students[name]=(students[name]+grade)/2

higher_average = {key: value for key, value in students.items() if value >= 4.5}

a = dict(sorted(higher_average.items(), key=lambda x: x[1], reverse=True))

for key, value in a.items():
    print(f'{key} -> {value:.2f}')
