rent=int(input())

cake_price=0.2*rent
beverage_price=cake_price-(0.45*cake_price)
entertainer_price=rent/3

total=rent+cake_price+beverage_price+entertainer_price

print(total)


