from collections import deque

cups=deque([int(cup) for cup in input().split()])
bottles=[int(bottle) for bottle in input().split()]

wasted_water=0

while cups and bottles:
    current_cup=cups.popleft()
    current_bottle=bottles.pop()
    if current_bottle>=current_cup:
        wasted_water+=current_bottle-current_cup
    else:
        current_cup-=current_bottle
        cups.appendleft(current_cup)

if bottles:
    bottles=[str(b) for b in bottles]
    print(f'Bottles: {" ".join(bottles)}')

if cups:
    cups=[str(c) for c in cups]
    print(f'Cups: {" ".join(cups)}')

print(f'Wasted litters of water: {wasted_water}')
