def indices_validator(row, column, size):
    if 0 <= row < size and 0 <= column < size:
        return True
    return False


n = int(input())

field = [[el for el in input()] for _ in range(n)]

snake_row = 0
snake_column = 0
burrows = []

for r in range(n):
    for c in range(n):
        if field[r][c] == 'S':
            snake_row = r
            snake_column = c
        elif field[r][c] == 'B':
            burrows.append([r, c])

food = 0
game_over=False

while food < 10:
    command = input()
    if command == 'up' and indices_validator(snake_row - 1, snake_column, n):
        field[snake_row][snake_column] = '.'
        snake_row -= 1
    elif command == 'down' and indices_validator(snake_row + 1, snake_column, n):
        field[snake_row][snake_column] = '.'
        snake_row += 1
    elif command == 'left' and indices_validator(snake_row, snake_column - 1, n):
        field[snake_row][snake_column] = '.'
        snake_column -= 1
    elif command == 'right' and indices_validator(snake_row, snake_column + 1, n):
        field[snake_row][snake_column] = '.'
        snake_column += 1
    else:
        field[snake_row][snake_column] = '.'
        game_over=True
        break

    if field[snake_row][snake_column] == '*':
        food+=1
        field[snake_row][snake_column]='S'
    elif field[snake_row][snake_column]=='B':
        field[snake_row][snake_column]='.'
        position_of_first_burrow=[snake_row, snake_column]
        for el in burrows:
            if not position_of_first_burrow==el:
                snake_row=el[0]
                snake_column=el[1]
        field[snake_row][snake_column]='S'
    else:
        field[snake_row][snake_column]='S'

if game_over:
    print('Game over!')
    print(f'Food eaten: {food}')
    for r in field:
        print(''.join(r))
else:
    print('You won! You fed the snake.')
    print(f'Food eaten: {food}')
    for r in field:
        print(''.join(r))