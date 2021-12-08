from collections import deque

bees=deque([int(el) for el in input().split()])
nectar=[int(el) for el in input().split()]
actions=deque(input().split())

honey=0

while nectar and bees:
    matched=False
    bee_number=bees.popleft()
    while nectar:
        nectar_number = nectar.pop()
        if nectar_number>=bee_number:
            matched=True
            action=actions.popleft()
            if not (action=='/' and nectar_number==0):
                result=abs(eval(f'{bee_number} {action} {nectar_number}'))
                honey+=result
                break
    if not matched:
        bees.appendleft(bee_number)


print(f'Total honey made: {honey}')

bees=[str(el) for el in bees]
if bees:
    print(f'Bees left: {", ".join(bees)}')

nectar=[str(n) for n in nectar]
if nectar:
    print(f'Nectar left: {", ".join(nectar)}')

