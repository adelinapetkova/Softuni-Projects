import math

name=input()
budget=float(input())
bottles_of_beer=int(input())
packages_chips=int(input())

beer_price=1.20
chips_price=beer_price*bottles_of_beer*0.45

total=bottles_of_beer*beer_price+math.ceil(chips_price*packages_chips)

if budget>=total:
    left=budget-total
    print(f'{name} bought a snack and has {left:.2f} leva left.')
else:
    needed=total-budget
    print(f'{name} needs {needed:.2f} more leva!')