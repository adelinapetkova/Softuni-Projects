budget=float(input())
number_of_extras=int(input())
price_of_a_costume=float(input())

decor=0.1*budget
money_for_costumes=number_of_extras*price_of_a_costume

if number_of_extras>150:
    money_for_costumes=money_for_costumes*0.9

total=decor+money_for_costumes

if total>budget:
    print('Not enough money!')
    needed=total-budget
    print(f'Wingard needs {needed:.2f} leva more.')
else:
    print('Action!')
    remainder=budget-total
    print(f'Wingard starts filming with {remainder:.2f} leva left.')
