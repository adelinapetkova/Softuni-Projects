budget=float(input())
season=input()

price=0
destination=''
place=''

if budget<=100:
    destination='Bulgaria'
    if season=='summer':
        price=0.3*budget
        place='Camp'
    elif season=='winter':
        price=0.7*budget
        place='Hotel'
elif 100<budget<=1000:
    destination='Balkans'
    if season=='summer':
        price=0.4*budget
        place='Camp'
    elif season=='winter':
        price=0.8*budget
        place='Hotel'
else:
    destination='Europe'
    price=0.9*budget
    place='Hotel'

print(f'Somewhere in {destination}')
print(f'{place} - {price:.2f}')