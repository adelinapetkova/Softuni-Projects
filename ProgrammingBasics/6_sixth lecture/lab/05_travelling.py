destination=input()

while destination!='End':
    budget=int(input())
    saved_money=0

    while saved_money<budget:
        money=int(input())
        saved_money+=money
    print(f'Going to {destination}!')
    destination=input()
