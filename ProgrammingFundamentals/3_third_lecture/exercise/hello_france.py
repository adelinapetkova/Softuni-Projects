pricelist=input().split('|')
budget=float(input())

profit=0
sum_for_france=0

for item in pricelist:
    new_price = 0
    prod=item.split('->')
    product=prod[0]
    price_of_product=float(prod[1])
    if price_of_product>budget:
        continue
    if product=='Clothes' and price_of_product<=50.00:
        budget-=price_of_product
        profit+=40*price_of_product/100
        new_price=140*price_of_product/100
        print(f'{new_price:.2f}', end=' ')
    elif product == 'Shoes' and price_of_product <= 35.00:
        budget -= price_of_product
        profit += 40 * price_of_product / 100
        new_price = 140 * price_of_product / 100
        print(f'{new_price:.2f}', end=' ')
    elif product == 'Accessories' and price_of_product <= 20.50:
        budget -= price_of_product
        profit += 40 * price_of_product / 100
        new_price = 140 * price_of_product / 100
        print(f'{new_price:.2f}', end=' ')
    sum_for_france+=new_price

print()
print(f'Profit: {profit:.2f}')
total=sum_for_france+budget
if total>=150:
    print('Hello, France!')
else:
    print('Time to go.')
