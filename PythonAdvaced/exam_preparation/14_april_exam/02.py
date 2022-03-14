size = 7

first_player, second_player = input().split(', ')
board = [[el for el in input().split()] for _ in range(size)]

first_player_score = 501
second_player_score = 501

num_of_round = 1
found_winner = False
fp_turns = 0
sp_turns = 0
winner = ''

while not found_winner:
    if num_of_round % 2 == 1:
        current_player = first_player
        current_player_score = first_player_score
        fp_turns += 1
    else:
        current_player = second_player
        current_player_score = second_player_score
        sp_turns += 1

    throw = input()
    row_column = []
    for el in throw:
        if el.isdigit():
            row_column.append(int(el))
    row = row_column[0]
    column = row_column[1]
    if not (0 <= row < size and 0 <= column < size):
        num_of_round += 1
        continue
    elif board[row][column].isdigit():
        current_player_score -= int(board[row][column])
    elif board[row][column] == 'D':
        sum_of_corresponding_numbers = int(board[0][column]) + int(board[size - 1][column]) + int(board[row][0]) + int(
            board[row][size - 1])
        current_player_score -= sum_of_corresponding_numbers * 2
    elif board[row][column] == 'T':
        sum_of_corresponding_numbers = int(board[0][column]) + int(board[size - 1][column]) + int(board[row][0]) + int(
            board[row][size - 1])
        current_player_score -= sum_of_corresponding_numbers * 3
    elif board[row][column] == 'B':
        found_winner = True
        winner = current_player
        break

    if current_player == first_player:
        first_player_score = current_player_score
    else:
        second_player_score = current_player_score

    if current_player_score <= 0:
        found_winner = True
        winner = current_player

    num_of_round += 1

if winner == first_player:
    print(f'{winner} won the game with {fp_turns} throws!')
else:
    print(f'{winner} won the game with {sp_turns} throws!')
