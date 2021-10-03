budget=float(input())
actor=input()

while actor!='ACTION':
    if len(actor)>15:
        paycheck=0.2*budget
    else:
        paycheck=float(input())
    budget-=paycheck
    if budget<=0:
        break
    actor=input()

if budget<=0:
    print(f'We need {abs(budget):.2f} leva for our actors.')
else:
    print(f'We are left with {budget:.2f} leva.')