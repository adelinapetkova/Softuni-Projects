n = int(input())
plants = {}

for _ in range(n):
    plant, rarity = input().split('<->')
    if plant not in plants:
        plants[plant] = {}
        plants[plant]['rarity'] = int(rarity)
        plants[plant]['rating'] = []
    else:
        plants[plant]['rarity'] = int(rarity)

command = input()

while not command == 'Exhibition':
    if 'Rate' in command:
        action, info = command.split(': ')
        plant, rating = info.split(' - ')
        rating = int(rating)
        if plant in plants:
            plants[plant]['rating'].append(rating)
        else:
            print('error')
    elif 'Update' in command:
        action, info = command.split(': ')
        plant, rarity = info.split(' - ')
        rarity = int(rarity)
        if plant in plants:
            plants[plant]['rarity'] = rarity
        else:
            print('error')
    elif 'Reset' in command:
        action, plant = command.split(': ')
        if plant in plants:
            plants[plant]['rating'] = []
        else:
            print('error')
    command = input()

for plant, info in plants.items():
    if len(plants[plant]['rating']) == 0:
        plants[plant]['rating'] = 0
    else:
        plants[plant]['rating'] = sum(plants[plant]['rating']) / len(plants[plant]['rating'])

sorted_dictionary = dict(sorted(plants.items(), key=lambda x: (-x[1]['rarity'], -x[1]['rating'])))

print('Plants for the exhibition:')

for plant, info in sorted_dictionary.items():
    print(f'- {plant}; Rarity: {plants[plant]["rarity"]}; Rating: {plants[plant]["rating"]:.2f}')
