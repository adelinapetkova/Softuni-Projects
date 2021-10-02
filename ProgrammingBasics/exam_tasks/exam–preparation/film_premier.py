movie=input()
food=input()
tickets=int(input())
price=0
total=0

if movie=='John Wick':
    if food=='Drink':
        price=12
    elif food=='Popcorn':
        price=15
    else:
        price=19
    total=price*tickets
elif movie=='Star Wars':
    if food=='Drink':
        price=18
    elif food=='Popcorn':
        price=25
    else:
        price=30
    total = price * tickets
    if tickets>=4:
        total=total*0.7
elif movie=='Jumanji':
    if food=='Drink':
        price=9
    elif food=='Popcorn':
        price=11
    else:
        price=14
    total = price * tickets
    if tickets==2:
        total=0.85*total

print(f'Your bill is {total:.2f} leva.')