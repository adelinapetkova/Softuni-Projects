import math

figure_type=input()

S=0

if figure_type=='square':
    a=float(input())
    S=a*a
elif figure_type=='rectangle':
    a=float(input())
    b=float(input())
    S=a*b
elif figure_type=='circle':
    r=float(input())
    S=math.pi*r**2
elif figure_type=='triangle':
    a=float(input())
    ha=float(input())
    S=a*ha/2
print(f'{S:.3f}')