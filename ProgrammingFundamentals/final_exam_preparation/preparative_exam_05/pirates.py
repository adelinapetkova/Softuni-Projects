town = input()
towns = {}

while not town == 'Sail':
    city, population, gold = town.split('||')
    population = int(population)
    gold = int(gold)
    if city not in towns:
        towns[city] = {}
        towns[city]['population'] = population
        towns[city]['gold'] = gold
    else:
        towns[city]['population'] += population
        towns[city]['gold'] += gold
    town = input()

event = input()

while not event == 'End':
    if 'Plunder' in event:
        action, town, people, gold = event.split('=>')
        people = int(people)
        gold = int(gold)
        towns[town]['population'] -= people
        towns[town]['gold'] -= gold
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        if towns[town]['population'] <= 0 or towns[town]['gold'] <= 0:
            towns.pop(town)
            print(f"{town} has been wiped off the map!")
    elif 'Prosper' in event:
        action, town, gold = event.split('=>')
        gold = int(gold)
        if gold < 0:
            print('Gold added cannot be a negative number!')
        else:
            towns[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {towns[town]['gold']} gold.")
    event = input()

sorted_towns = dict(sorted(towns.items(), key=lambda x: (-x[1]['gold'], x[0])))

if len(sorted_towns) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f'Ahoy, Captain! There are {len(sorted_towns)} wealthy settlements to go to:')
    for t in sorted_towns:
        print(f'{t} -> Population: {towns[t]["population"]} citizens, Gold: {towns[t]["gold"]} kg')
