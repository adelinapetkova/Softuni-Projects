budget=int(input())
season=input()
fishermen=int(input())

price=0
discount=0

if season=='Spring':
    price=3000
elif season=='Summer' or season=='Autumn':
    price=4200
elif season=='Winter':
    price=2600

if fishermen<=6:
    discount=0.1
elif 7<=fishermen<=11:
    discount=0.15
else:
    discount=0.25

total=price-(price*discount)

second_discount=0

if fishermen%2==0 and season!='Autumn':
    second_discount=0.05

final_price=total-(second_discount*total)

if budget>=final_price:
    left=budget-final_price
    print(f'Yes! You have {left:.2f} leva left.')
elif budget<final_price:
    needed=final_price-budget
    print(f'Not enough money! You need {needed:.2f} leva.')