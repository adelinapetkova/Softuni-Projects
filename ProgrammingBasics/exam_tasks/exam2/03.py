month=input()
hours=int(input())
people=int(input())
day_or_night=input()
price_per_person=0

if month=='march' or month=='april' or month=='may':
    if day_or_night=='day':
        price_per_person=10.50
    else:
        price_per_person=8.40
else:
    if day_or_night=='day':
        price_per_person=12.60
    else:
        price_per_person=10.20

if people>=4:
    price_per_person=price_per_person*0.9

if hours>=5:
    price_per_person=price_per_person*0.5

total=price_per_person*people*hours

print(f'Price per person for one hour: {price_per_person:.2f}')
print(f'Total cost of the visit: {total:.2f}')