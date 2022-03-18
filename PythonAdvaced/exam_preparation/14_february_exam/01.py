from collections import deque

firework_effects=deque([int(el) for el in input().split(', ')])
explosive_power=[int(el) for el in input().split(', ')]
fireworks={'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks':0}
enough_fireworks=False

while firework_effects and explosive_power:
    current_effect=firework_effects.popleft()
    current_power=explosive_power.pop()
    if current_effect<=0:
        explosive_power.append(current_power)
        continue
    if current_power<=0:
        firework_effects.appendleft(current_effect)
        continue
    sum_of_values=current_power+current_effect
    if sum_of_values%3==0 and sum_of_values%5==0:
        fireworks['Crossette Fireworks']+=1
    elif sum_of_values%3==0:
        fireworks['Palm Fireworks']+=1
    elif sum_of_values%5==0:
        fireworks['Willow Fireworks']+=1
    else:
        current_effect-=1
        firework_effects.append(current_effect)
        explosive_power.append(current_power)

    enough_fireworks=True
    for value in fireworks.values():
        if value<3:
            enough_fireworks=False
            break

    if enough_fireworks:
        break


if enough_fireworks:
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    firework_effects=[str(el) for el in firework_effects]
    print(f'Firework Effects left: {", ".join(firework_effects)}')

if explosive_power:
    explosive_power=[str(el) for el in explosive_power]
    print(f'Explosive Power left: {", ".join(explosive_power)}')

for key, value in fireworks.items():
    print(f'{key}: {value}')




