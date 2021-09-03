trip_price=float(input())

puzzles=int(input())
dolls=int(input())
bears=int(input())
minions=int(input())
trucks=int(input())

puzzle_price=2.60
doll_price=3.00
bear_price=4.10
minion_price=8.20
truck_price=2.00

money_from_puzzles=puzzles*puzzle_price
money_from_dolls=dolls*doll_price
money_from_bears=bears*bear_price
money_from_minions=minions*minion_price
money_from_trucks=trucks*truck_price

total=money_from_trucks+money_from_minions+money_from_bears+money_from_dolls+money_from_puzzles

amount_of_toys=puzzles+dolls+bears+minions+trucks

if amount_of_toys>=50:
    discount=25*total/100
    total=total-discount

final=total-(10*total/100)

if final>=trip_price:
    remainder=final-trip_price
    print(f'Yes! {remainder:.2f} lv left.')
else:
    shortage=trip_price-final
    print(f'Not enough money! {shortage:.2f} lv needed.')




