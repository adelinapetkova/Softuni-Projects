from collections import deque

males=[int(el) for el in input().split()]
females=deque([int(el) for el in input().split()])
matches=0

while males and females:
    current_male=males.pop()
    current_female = females.popleft()
    if current_male < 1:
        females.appendleft(current_female)
        continue

    if current_female < 1:
        males.append(current_male)
        continue

    if current_male%25==0:
        males.pop()
        females.appendleft(current_female)
        continue
    if current_female%25==0:
        females.popleft()
        males.append(current_male)
        continue

    if current_female==current_male:
        matches+=1
    else:
        current_male-=2
        if current_male>0:
            males.append(current_male)


print(f'Matches: {matches}')
if males:
    males = [str(el) for el in males]
    print(f'Males left: {", ".join(list(reversed(males)))}')
else:
    print('Males left: none')

if females:
    females = [str(el) for el in females]
    print(f'Females left: {", ".join(females)}')
else:
    print('Females left: none')
