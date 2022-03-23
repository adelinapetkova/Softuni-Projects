size = int(input())
num_of_bombs = int(input())

field = [[' ' for i in range(size)] for _ in range(size)]
coordinates_of_bombs = []

for i in range(num_of_bombs):
    text = input()
    coordinates=[]
    for ch in text:
        if ch.isdigit():
            coordinates.append(int(ch))
    if 0 <= coordinates[0] < size and 0 <= coordinates[1] < size:
        field[coordinates[0]][coordinates[1]] = "*"

    coordinates_of_bombs.append(coordinates)


elements_near_current_position = []
number = 0

for r in range(size):
    for c in range(size):
        if not field[r][c] == '*':
            number = 0
            elements_near_current_position = [[r - 1, c - 1], [r - 1, c], [r - 1, c + 1], [r, c - 1], [r, c + 1],
                                              [r + 1, c - 1], [r + 1, c], [r + 1, c + 1]]
            for el in elements_near_current_position:
                if el in coordinates_of_bombs:
                    number += 1

            field[r][c] = str(number)

for row in field:
    print(' '.join(row))
