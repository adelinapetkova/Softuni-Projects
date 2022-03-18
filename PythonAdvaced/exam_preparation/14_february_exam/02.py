import math


def indices_validator(row, column, board_size):
    if 0 <= row < board_size and 0 <= column < board_size:
        return True
    return False


size = int(input())

board = [[el for el in input().split()] for _ in range(size)]

coins = 0
path = []

player_row = 0
player_col = 0

for r in range(size):
    for c in range(size):
        if board[r][c] == 'P':
            player_col = c
            player_row = r
            break

while coins < 100:
    movement = input()

    if movement == 'up':
        if indices_validator(player_row - 1, player_col, size):
            player_row -= 1
            if board[player_row][player_col] == 'X':
                coins = math.floor(coins / 2)
                break
            else:
                coins += int(board[player_row][player_col])
                path.append([player_row, player_col])
        else:
            coins = math.floor(coins / 2)
            break
    elif movement == 'down':
        if indices_validator(player_row + 1, player_col, size):
            player_row += 1
            if board[player_row][player_col] == 'X':
                coins = math.floor(coins / 2)
                break
            else:
                coins += int(board[player_row][player_col])
                path.append([player_row, player_col])
        else:
            coins = math.floor(coins / 2)
            break
    elif movement == 'left':
        if indices_validator(player_row, player_col - 1, size):
            player_col -= 1
            if board[player_row][player_col] == 'X':
                coins = math.floor(coins / 2)
                break
            else:
                coins += int(board[player_row][player_col])
                path.append([player_row, player_col])
        else:
            coins = math.floor(coins / 2)
            break
    elif movement == 'right':
        if indices_validator(player_row, player_col + 1, size):
            player_col += 1
            if board[player_row][player_col] == 'X':
                coins = math.floor(coins / 2)
                break
            else:
                coins += int(board[player_row][player_col])
                path.append([player_row, player_col])
        else:
            coins = math.floor(coins / 2)
            break
    else:
        continue


if coins>=100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print('Your path:')

for move in path:
    print(move)