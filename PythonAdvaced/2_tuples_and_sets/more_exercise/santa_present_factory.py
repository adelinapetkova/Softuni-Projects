from collections import deque

materials = [int(num) for num in input().split()]
magic_level = deque([int(num) for num in input().split()])

presents = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0,
}

while materials and magic_level:
    material_num = materials.pop()
    magic_level_num = magic_level.popleft()
    result = material_num * magic_level_num
    if result == 150:
        presents['Doll'] += 1
    elif result == 250:
        presents['Wooden train'] += 1
    elif result == 300:
        presents['Teddy bear'] += 1
    elif result == 400:
        presents['Bicycle'] += 1
    else:
        if result < 0:
            sum_for_material = material_num + magic_level_num
            materials.append(sum_for_material)
        elif result == 0:
            if not material_num == 0:
                materials.append(material_num)
            if not magic_level_num == 0:
                magic_level.appendleft(magic_level_num)
        else:
            material_num += 15
            materials.append(material_num)

if (presents['Doll'] > 0 and presents['Wooden train'] > 0) or (presents['Teddy bear'] > 0 and presents['Bicycle'] > 0):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    materials = [str(el) for el in materials]
    print(f'Materials left: {", ".join(reversed(materials))}')

if magic_level:
    magic_level = [str(el) for el in magic_level]
    print(f'Magic left: {", ".join(magic_level)}')

presents = dict(sorted(presents.items(), key=lambda x: x[0]))

for present, quantity in presents.items():
    if quantity > 0:
        print(f'{present}: {quantity}')
