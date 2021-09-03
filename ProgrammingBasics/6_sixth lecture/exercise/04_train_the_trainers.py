grades_per_presentation=int(input())
presentation=input()
grade_sum=0
total_grade_for_presentation=0
total_grade=0
num_presentations=0

while presentation!='Finish':
    num_presentations+=1
    grades_for_presentation=0
    for i in range(grades_per_presentation):
        grade=float(input())
        grades_for_presentation+=grade
        total_grade_for_presentation=grades_for_presentation/grades_per_presentation
        grade_sum+=grade
    print(f'{presentation} - {total_grade_for_presentation:.2f}.')
    presentation=input()

total_grade=grade_sum/(num_presentations*grades_per_presentation)
print(f"Student's final assessment is {total_grade:.2f}.")
