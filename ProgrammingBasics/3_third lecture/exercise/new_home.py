flower_type=input()
flower_quantity=int(input())
budget=int(input())

rose_price=5.00
dahlia_price=3.80
tulip_price=2.80
narciss_price=3.00
gladiol_price=2.50

price=0

if flower_type=='Roses':
    if flower_quantity>80:
        price=0.9*flower_quantity*rose_price
    else:
        price=flower_quantity*rose_price
elif flower_type=='Dahlias':
    if flower_quantity>90:
        price=flower_quantity*dahlia_price*0.85
    else:
        price=flower_quantity*dahlia_price
elif flower_type=='Tulips':
    if flower_quantity>80:
        price=flower_quantity*tulip_price*0.85
    else:
        price=flower_quantity*tulip_price
elif flower_type=='Narcissus':
    if flower_quantity<120:
        price=flower_quantity*narciss_price*1.15
    else:
        price=flower_quantity*narciss_price
elif flower_type=='Gladiolus':
    if flower_quantity<80:
        price=flower_quantity*gladiol_price*1.2
    else:
        price=flower_quantity*gladiol_price

if budget>=price:
    left=budget-price
    print(f'Hey, you have a great garden with {flower_quantity} {flower_type} and {left:.2f} leva left.')
else:
    needed=price-budget
    print(f'Not enough money, you need {needed:.2f} leva more.')
