name=input()

class_count=1
bad_grades=0
sum=0
classes=0

while class_count<=12:
    grade = float(input())
    if grade<4.00:
        class_count-=1
        bad_grades+=1
    classes+=1
    if bad_grades>1:
        break
    sum += grade
    class_count+=1

if class_count-1==12:
    print(f'{name} graduated. Average grade: {(sum/classes):.2f}')
elif class_count<12:
    print(f'{name} has been excluded at {class_count+1} grade')

