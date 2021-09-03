import math

square_meters=int(input())
kg_grapes_per_sq_m=float(input())
needed_liters=int(input())
workers=int(input())

sq_meters_for_wine=40*square_meters/100
kg_grapes=sq_meters_for_wine*kg_grapes_per_sq_m
liters_wine=kg_grapes/2.5

if liters_wine<needed_liters:
    needed_wine=math.floor(needed_liters-liters_wine)
    print(f'It will be a tough winter! More {needed_wine} liters wine needed.')
elif liters_wine>=needed_liters:
    print(f'Good harvest this year! Total wine: {math.floor(liters_wine)} liters.')
    left_wine=math.ceil(liters_wine-needed_liters)
    wine_per_worker=math.ceil(left_wine/workers)
    print(f'{left_wine} liters left -> {wine_per_worker} liters per person.')
