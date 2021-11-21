from collections import deque

liters_in_dispenser = int(input())

names = input()
people = deque()

while not names == 'Start':
    people.append(names)
    names = input()

command = input()

while not command == 'End':
    if 'refill' not in command:
        if liters_in_dispenser >= int(command):
            liters_in_dispenser -= int(command)
            print(f'{people.popleft()} got water')
        else:
            print(f'{people.popleft()} must wait')
    else:
        action, liters = command.split()
        liters = int(liters)
        liters_in_dispenser += liters
    command = input()

print(f'{liters_in_dispenser} liters left')
