from collections import deque


def get_player_choice(num_of_player):
    print(f'Player {player}, please choose a column')
    number_of_column = int(input())
    return number_of_column - 1


def apply_player_choice(board_place, player_column, num_of_player):
    wanted_column = []
    for i in range(6):
        wanted_column.append(board_place[i][player_column])

    row_changed = 0
    for j in range(len(wanted_column)):
        if not wanted_column[j] == 0:
            board_place[j - 1][player_column] = num_of_player
            row_changed = j
            break
        if j == 5:
            row_changed = 5
            board_place[j][player_column] = num_of_player

    return board_place, row_changed


def check_win_condition(board_place, position_column, position_row, num_of_player, winner):
    current_column = []
    current_row = []
    left_diagonal = deque()
    right_diagonal = deque()
    searched_pattern = [str(num_of_player)] * 4
    searched_pattern = ''.join(searched_pattern)

    current_row = board_place[position_row]

    for i in range(6):
        current_column.append(board_place[i][position_column])

    ld_row = position_row-1
    ld_column = position_column
    while 0 <= ld_row < 6 and 0 <= ld_column < 7:
        left_diagonal.appendleft(board_place[ld_row][ld_column])
        ld_row -= 1
        ld_column -= 1

    ld_row = position_row-1
    ld_column = position_column
    k = 0
    while 0 <= ld_row < 6 and 0 <= ld_column < 7:
        if k == 0:
            k += 1
            ld_row += 1
            ld_column += 1
            continue
        left_diagonal.append(board_place[ld_row][ld_column])
        ld_row += 1
        ld_column += 1
        k += 1

    rd_row = position_row-1
    rd_column = position_column
    while 0 <= rd_row < 6 and 0 <= rd_column < 7:
        right_diagonal.appendleft(board_place[rd_row][rd_column])
        rd_row += 1
        rd_column -= 1

    rd_row = position_row-1
    rd_column = position_column
    k = 0
    while 0 <= rd_row < 6 and 0 <= rd_column < 7:
        if k == 0:
            k += 1
            rd_row -= 1
            rd_column += 1
            continue
        right_diagonal.append(board_place[rd_row][rd_column])
        rd_row -= 1
        rd_column += 1
        k += 1

    current_row = ''.join([str(el) for el in current_row])
    current_column = ''.join([str(el) for el in current_column])
    left_diagonal = ''.join([str(el) for el in left_diagonal])
    right_diagonal = ''.join([str(el) for el in right_diagonal])

    if searched_pattern in current_row or searched_pattern in current_column:
        winner = True
    elif searched_pattern in left_diagonal or searched_pattern in right_diagonal:
        winner = True

    return winner


def play(number):
    num_of_player = 0
    if number % 2 == 1:
        num_of_player = 1
    else:
        num_of_player = 2

    return num_of_player


found_winner = False
board = [[0, 0, 0, 0, 0, 0, 0] for _ in range(6)]

round_number = 0
number_of_winner = 0
while not found_winner:
    round_number += 1
    player = play(round_number)
    column = get_player_choice(player)
    board, row_that_changed = apply_player_choice(board, column, player)
    found_winner = check_win_condition(board, column, row_that_changed, player, found_winner)
    if found_winner:
        number_of_winner = player

    for r in board:
        print(r)

print(f'The winner is player {number_of_winner}')
