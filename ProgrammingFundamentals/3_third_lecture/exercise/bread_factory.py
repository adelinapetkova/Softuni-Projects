energy = 100
coins = 100
events = input().split('|')

for event in events:
    even = event.split('-')
    activity = even[0]
    cost = int(even[1])
    if activity == 'rest':
        if energy + cost > 100:
            print('You gained 0 energy.')
        else:
            print(f'You gained {cost} energy.')
            energy += cost
        print(f'Current energy: {energy}.')
    elif activity == 'order':
        if energy >= 30:
            coins += cost
            energy -= 30
            print(f'You earned {cost} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins - cost > 0:
            coins -= cost
            print(f'You bought {activity}.')
        else:
            print(f'Closed! Cannot afford {activity}.')
            coins -= cost
            break

if not coins <= 0:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
