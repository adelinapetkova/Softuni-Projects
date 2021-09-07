fires = input().split('#')
water = int(input())

effort = 0
total_fire = 0

print('Cells:')

for element in fires:
    fire = element.split(' = ')
    level_of_fire = fire[0]
    liters_per_fire = fire[1]
    if int(liters_per_fire) > water:
        continue
    if level_of_fire == 'High' and 81 <= int(liters_per_fire) <= 125:
        water -= int(liters_per_fire)
        total_fire += int(liters_per_fire)
        effort += (25 * int(liters_per_fire)) / 100
        print(f'- {liters_per_fire}')
    elif level_of_fire == 'Medium' and 51 <= int(liters_per_fire) <= 80:
        water -= int(liters_per_fire)
        total_fire += int(liters_per_fire)
        effort += (25 * int(liters_per_fire)) / 100
        print(f'- {liters_per_fire}')
    elif level_of_fire == 'Low' and 1 <= int(liters_per_fire) <= 50:
        water -= int(liters_per_fire)
        total_fire += int(liters_per_fire)
        effort += (25 * int(liters_per_fire)) / 100
        print(f'- {liters_per_fire}')


print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
