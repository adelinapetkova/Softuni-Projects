n = int(input())
cars = {}

for _ in range(n):
    car, mileage, fuel = input().split('|')
    mileage = int(mileage)
    fuel = int(fuel)
    cars[car] = {}
    cars[car]['mileage'] = mileage
    cars[car]['fuel'] = fuel

command = input()

while not command == 'Stop':
    if 'Drive' in command:
        action, car, distance, fuel = command.split(' : ')
        distance = int(distance)
        fuel = int(fuel)
        if fuel > cars[car]['fuel']:
            print('Not enough fuel to make that ride')
        else:
            cars[car]['mileage'] += distance
            cars[car]['fuel'] -= fuel
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        if cars[car]['mileage'] >= 100000:
            cars.pop(car)
            print(f'Time to sell the {car}!')
    elif 'Refuel' in command:
        action, car, fuel = command.split(' : ')
        fuel = int(fuel)
        max_amount_fuel_to_fit = 75 - cars[car]['fuel']
        if fuel > max_amount_fuel_to_fit:
            cars[car]['fuel'] = 75
            print(f'{car} refueled with {max_amount_fuel_to_fit} liters')
        else:
            cars[car]['fuel'] += fuel
            print(f'{car} refueled with {fuel} liters')
    elif 'Revert' in command:
        action, car, km = command.split(' : ')
        km = int(km)
        cars[car]['mileage'] -= km
        if cars[car]['mileage'] < 10000:
            cars[car]['mileage'] = 10000
        else:
            print(f'{car} mileage decreased by {km} kilometers')
    command = input()

sorted_cars = dict(sorted(cars.items(), key=lambda x: (-x[1]['mileage'], x[0])))

for car, info in sorted_cars.items():
    print(f'{car} -> Mileage: {cars[car]["mileage"]} kms, Fuel in the tank: {cars[car]["fuel"]} lt.')
