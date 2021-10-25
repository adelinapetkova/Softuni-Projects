import math

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
maximum_bonus = 0
max_bonus_attendances = 0

for student in range(1, number_of_students + 1):
    attendances = int(input())
    total_bonus = attendances / number_of_lectures * (5 + additional_bonus)
    if total_bonus >= maximum_bonus:
        maximum_bonus = total_bonus
        max_bonus_attendances = attendances

print(f"Max Bonus: {math.ceil(maximum_bonus)}.")
print(f"The student has attended {round(max_bonus_attendances)} lectures.")
