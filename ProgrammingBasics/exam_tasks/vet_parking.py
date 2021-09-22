days=int(input())
hours_per_day=int(input())

price=0
total=0

for day in range(1,days+1):
    day_price = 0
    for hour in range(1,hours_per_day+1):
        if day%2==0 and hour%2==1:
            price=2.50
        elif day%2==1 and hour%2==0:
            price=1.25
        else:
            price=1
        day_price+=price
    print(f'Day: {day} - {day_price:.2f} leva')
    total+=day_price
print(f'Total: {total:.2f} leva')