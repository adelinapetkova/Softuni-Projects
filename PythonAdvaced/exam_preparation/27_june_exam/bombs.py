from collections import deque

bomb_effects = deque([int(el) for el in input().split(', ')])
bomb_casings = [int(el) for el in input().split(', ')]
bombs = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
enough_bombs = True

while bomb_effects and bomb_casings:
    enough_bombs = True
    for value in bombs.values():
        if not value >= 3:
            enough_bombs = False
            break

    if enough_bombs:
        break

    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()

    result = current_effect + current_casing

    if result == 40:
        bombs['Datura Bombs'] += 1
    elif result == 60:
        bombs['Cherry Bombs'] += 1
    elif result == 120:
        bombs['Smoke Decoy Bombs'] += 1
    else:
        current_casing -= 5
        bomb_casings.append(current_casing)
        bomb_effects.appendleft(current_effect)

if enough_bombs:
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    bomb_effects = [str(el) for el in bomb_effects]
    print(f'Bomb Effects: {", ".join(bomb_effects)}')
else:
    print('Bomb Effects: empty')

if bomb_casings:
    bomb_casings = [str(el) for el in bomb_casings]
    print(f'Bomb Casings: {", ".join(bomb_casings)}')
else:
    print('Bomb Casings: empty')

bombs = dict(sorted(bombs.items(), key=lambda x: x[0]))

for key, value in bombs.items():
    print(f'{key}: {value}')
