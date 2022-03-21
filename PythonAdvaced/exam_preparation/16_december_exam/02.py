def indices_validator(row, column, size_of_field):
    if 0 <= row < size_of_field and 0 <= column < size_of_field:
        return True
    return False


text = [el for el in input()]
size = int(input())

current_row = 0
current_col = 0

field = [[el for el in input()] for _ in range(size)]
for r in range(size):
    for c in range(size):
        if field[r][c] == 'P':
            current_col = c
            current_row = r
            break

commands = int(input())

for i in range(commands):
    move = input()
    if move == 'up':
        if indices_validator(current_row - 1, current_col, size):
            field[current_row][current_col] = '-'
            current_row -= 1
            if not field[current_row][current_col] == '-':
                text.append(field[current_row][current_col])
                field[current_row][current_col] = 'P'
        else:
            if text:
                text.pop()
    elif move == 'down':
        if indices_validator(current_row + 1, current_col, size):
            field[current_row][current_col] = '-'
            current_row += 1
            if not field[current_row][current_col] == '-':
                text.append(field[current_row][current_col])
                field[current_row][current_col] = 'P'
        else:
            if text:
                text.pop()
    elif move == 'left':
        if indices_validator(current_row, current_col - 1, size):
            field[current_row][current_col] = '-'
            current_col -= 1
            if not field[current_row][current_col] == '-':
                text.append(field[current_row][current_col])
                field[current_row][current_col] = 'P'
        else:
            if text:
                text.pop()
    elif move == 'right':
        if indices_validator(current_row, current_col + 1, size):
            field[current_row][current_col] = '-'
            current_col += 1
            if not field[current_row][current_col] == '-':
                text.append(field[current_row][current_col])
                field[current_row][current_col] = 'P'
        else:
            if text:
                text.pop()

print(''.join(text))
for row in field:
    print(''.join(row))
