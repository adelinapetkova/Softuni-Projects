from collections import deque

materials = [int(el) for el in input().split()]
magic_levels = deque([int(el) for el in input().split()])

gifts = {'Gemstone': 0, 'Porcelain Sculpture': 0, 'Gold': 0, 'Diamond Jewellery': 0}

while materials and magic_levels:
    current_material = materials.pop()
    current_magic_level = magic_levels.popleft()

    sum_of_products = current_material + current_magic_level

    if 100 <= sum_of_products <= 199:
        gifts['Gemstone'] += 1
    elif 200 <= sum_of_products <= 299:
        gifts['Porcelain Sculpture'] += 1
    elif 300 <= sum_of_products <= 399:
        gifts['Gold'] += 1
    elif 400 <= sum_of_products <= 499:
        gifts['Diamond Jewellery'] += 1
    elif sum_of_products < 100:
        if sum_of_products % 2 == 0:
            current_material = current_material * 2
            current_magic_level = current_magic_level * 3
            sum_of_products = current_material + current_magic_level
            if 100 <= sum_of_products <= 199:
                gifts['Gemstone'] += 1
            elif 200 <= sum_of_products <= 299:
                gifts['Porcelain Sculpture'] += 1
            elif 300 <= sum_of_products <= 399:
                gifts['Gold'] += 1
            elif 400 <= sum_of_products <= 499:
                gifts['Diamond Jewellery'] += 1
        else:
            sum_of_products = sum_of_products * 2
            if 100 <= sum_of_products <= 199:
                gifts['Gemstone'] += 1
            elif 200 <= sum_of_products <= 299:
                gifts['Porcelain Sculpture'] += 1
            elif 300 <= sum_of_products <= 399:
                gifts['Gold'] += 1
            elif 400 <= sum_of_products <= 499:
                gifts['Diamond Jewellery'] += 1
    elif sum_of_products > 499:
        sum_of_products /= 2
        if 100 <= sum_of_products <= 199:
            gifts['Gemstone'] += 1
        elif 200 <= sum_of_products <= 299:
            gifts['Porcelain Sculpture'] += 1
        elif 300 <= sum_of_products <= 399:
            gifts['Gold'] += 1
        elif 400 <= sum_of_products <= 499:
            gifts['Diamond Jewellery'] += 1

enough_gifts = False

if (gifts['Gemstone'] > 0 and gifts['Porcelain Sculpture'] > 0) or (
        gifts['Gold'] > 0 and gifts['Diamond Jewellery'] > 0):
    enough_gifts = True

if enough_gifts:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if materials:
    materials = [str(el) for el in materials]
    print(f'Materials left: {", ".join(materials)}')

if magic_levels:
    magic_levels = [str(el) for el in magic_levels]
    print(f'Magic left: {", ".join(magic_levels)}')

gifts = dict(sorted(gifts.items(), key=lambda x: x[0]))

for key, value in gifts.items():
    if value > 0:
        print(f'{key}: {value}')
