def calculating_bill(product,quantity):
    if product=='coffee':
        return 1.50*quantity
    elif product=='water':
        return 1.00*quantity
    elif product=='coke':
        return 1.40*quantity
    elif product=='snacks':
        return 2.00*quantity

food=input()
n=int(input())

print(f'{calculating_bill(food,n):.2f}')