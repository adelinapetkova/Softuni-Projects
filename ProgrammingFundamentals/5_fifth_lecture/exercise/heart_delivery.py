houses = [int(el) for el in input().split('@')]
command = input().split()
cupid_position = 0

while not command[0] == 'Love!':
    if int(command[1]) + cupid_position >= len(houses):
        cupid_position = 0
        if houses[cupid_position] <= 0:
            print(f"Place {cupid_position} already had Valentine's day.")
            command = input().split()
            continue
        houses[cupid_position] -= 2
        if houses[cupid_position] <= 0:
            print(f"Place {cupid_position} has Valentine's day.")
    else:
        cupid_position += int(command[1])
        if houses[cupid_position] <= 0:
            print(f"Place {cupid_position} already had Valentine's day.")
            command = input().split()
            continue
        houses[cupid_position] -= 2
        if houses[cupid_position] <= 0:
            print(f"Place {cupid_position} has Valentine's day.")
    command = input().split()

print(f"Cupid's last position was {cupid_position}.")

failed_houses = [el for el in houses if not el == 0]

if len(failed_houses) == 0:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {len(failed_houses)} places.')
