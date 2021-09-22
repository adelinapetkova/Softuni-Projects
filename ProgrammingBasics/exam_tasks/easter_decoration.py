basket_price=1.5
wreath_price=3.8
chocolate_bunny_price=7
sum=0

number_of_clients=int(input())

for i in range(number_of_clients):
    total=0
    items=0
    product=input()
    while product!='Finish':
        items+=1
        if product=='basket':
            total+=basket_price
        elif product=='wreath':
            total+=wreath_price
        elif product=='chocolate bunny':
            total+=chocolate_bunny_price
        product=input()
    if items%2==0:
        total=total*0.8
    sum+=total
    print(f'You purchased {items} items for {total:.2f} leva.')

average=sum/number_of_clients
print(f'Average bill per client is: {average:.2f} leva.')


