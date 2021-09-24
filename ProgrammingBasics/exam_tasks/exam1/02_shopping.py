budget=float(input())
videocards=int(input())
procesors=int(input())
ram=int(input())

videocard_price=250
procesor_price=0.35*videocard_price*videocards
ram_price=0.1*videocard_price*videocards

total=videocard_price*videocards+procesor_price*procesors+ram_price*ram

if videocards>procesors:
    final=total*0.85
else:
    final=total

if budget>=final:
    print(f'You have {(budget-final):.2f} leva left!')
else:
    print(f'Not enough money! You need {(final-budget):.2f} leva more!')