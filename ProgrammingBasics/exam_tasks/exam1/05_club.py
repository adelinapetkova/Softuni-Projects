wanted_profit=float(input())
cocktail_type=input()

income=0


while cocktail_type!='Party!':
    quantity=int(input())
    cocktail_price=len(cocktail_type)
    money_from_order=cocktail_price*quantity
    if money_from_order%2==0:
        money_from_order = cocktail_price * quantity
    else:
        money_from_order=money_from_order*0.75
    income+=money_from_order
    if income>=wanted_profit:
        print('Target acquired.')
        break
    cocktail_type=input()

if income<wanted_profit:
    print(f'We need {(wanted_profit-income):.2f} leva more.')

print(f'Club income - {income:.2f} leva.')


