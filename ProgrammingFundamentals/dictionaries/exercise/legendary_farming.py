found_legendary_item = False
dictionary_materials = {}

while not found_legendary_item:
    materials = input().split()
    for i in range(1, len(materials) + 1, 2):
        if materials[i].lower() not in dictionary_materials:
            dictionary_materials[materials[i].lower()] = int(materials[i - 1])
        else:
            dictionary_materials[materials[i].lower()] += int(materials[i - 1])
        for key, value in dictionary_materials.items():
            if value >= 250 and key == 'shards':
                dictionary_materials[key] -= 250
                found_legendary_item = True
                print('Shadowmourne obtained!')
                break
            elif value >= 250 and key == 'fragments':
                dictionary_materials[key] -= 250
                found_legendary_item = True
                print('Valanyr obtained!')
                break
            elif value >= 250 and key == 'motes':
                dictionary_materials[key] -= 250
                found_legendary_item = True
                print('Dragonwrath obtained!')
                break
        if found_legendary_item:
            break

essential_materials = {'fragments': 0, 'shards': 0, 'motes': 0}
non_essential_materials = {}

for key, value in dictionary_materials.items():
    if key == 'shards' or key == 'fragments' or key == 'motes':
        essential_materials[key] += value
    else:
        non_essential_materials[key] = value

b = dict(sorted(essential_materials.items(), key=lambda x: (-x[1], x[0])))

for key, value in b.items():
    print(f'{key}: {value}')

c = dict(sorted(non_essential_materials.items(), key=lambda x: x[0]))

for key, value in c.items():
    print(f'{key}: {value}')
