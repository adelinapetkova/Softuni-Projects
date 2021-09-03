vacation_price=float(input())
saved_money=float(input())
spends=0
turns=0

while saved_money<vacation_price:
    turns+=1
    command=input()
    money=float(input())
    if command=='spend':
        if saved_money>money:
           saved_money-=money
        else:
            saved_money=0
        spends+=1
    elif command=='save':
        saved_money+=money
        spends=0
    if spends == 5:
        print("You can't save the money.")
        print(turns)
        break



if saved_money>=vacation_price:
    print(f'You saved the money for {turns} days.')