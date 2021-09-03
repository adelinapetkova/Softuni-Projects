import math

income=float(input())
grade=float(input())
min_salary=float(input())

if income<min_salary and grade>=5.5:
    social_scholarship=math.floor(0.35*min_salary)
    scholarship=math.floor(grade*25)
    if social_scholarship>scholarship:
        print(f'You get a Social scholarship {social_scholarship} BGN')
    elif scholarship>social_scholarship:
        print(f'You get a scholarship for excellent results {scholarship} BGN')
    elif scholarship==social_scholarship:
        print(f'You get a scholarship for excellent results {scholarship} BGN')
elif income<min_salary and grade>4.5:
    scholarship=math.floor(0.35*min_salary)
    print(f'You get a Social scholarship {scholarship} BGN')
elif grade>=5.5:
    scholarship=math.floor(grade*25)
    print(f'You get a scholarship for excellent results {scholarship} BGN')
elif income>min_salary and grade<5.5:
    print('You cannot get a scholarship!')
