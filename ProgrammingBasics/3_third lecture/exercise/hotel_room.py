month=input()
nights=int(input())

studio_price=0
apartment_price=0

if month=='May' or month=='October':
    studio_price=nights*50
    apartment_price=nights*65
    if nights>14:
        studio_price=nights*50*0.7
        apartment_price=nights*65*0.9
    elif nights>7:
        studio_price=nights*50*0.95
elif month=='June' or month=='September':
    studio_price=nights*75.20
    apartment_price=nights*68.70
    if nights>14:
        studio_price=nights*75.20*0.8
        apartment_price=nights*68.70*0.9
elif month=='July' or month=='August':
    studio_price=nights*76
    apartment_price=nights*77
    if nights>14:
        apartment_price=nights*77*0.9

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')


