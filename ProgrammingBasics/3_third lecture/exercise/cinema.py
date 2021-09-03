projection_type=input()
rows=int(input())
columns=int(input())

price=0

if projection_type=='Premiere':
    price=12
elif projection_type=='Normal':
    price=7.5
elif projection_type=='Discount':
    price=5

total=price*rows*columns

print(f'{total:.2f} leva')