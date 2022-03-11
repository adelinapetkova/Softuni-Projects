def get_player_info():
    first_player_name = input('Player one name: ')
    second_player_name = input('Player two name: ')
    first_player_sign = input(f"{first_player_name} would you like to play with 'X' or 'O'? ")
    if first_player_sign == 'X':
        second_player_sign = 'O'
    else:
        second_player_sign = 'X'

    return {first_player_name: first_player_sign, second_player_name: second_player_sign}


def numeration_of_board():
    print('This is the numeration of the board:')
    print('| 1 | 2 | 3 |')
    print('| 4 | 5 | 6 |')
    print('| 7 | 8 | 9 |')


def turns(round_number, name1, name2):
    if round_number % 2 == 1:
        return name1
    else:
        return name2


def get_player_choice(name):
    choice = int(input(f'{name} choose a free position [1-9]: '))
    return choice


def get_position(choice):
    if not choice % 3 == 0:
        row = choice // 3
        column = (choice % 3) - 1
    else:
        row = (choice // 3) - 1
        column = 2

    return [row, column]


def apply_players_choice(board, choice_row, choice_column, player_sign):
    board[choice_row][choice_column] = player_sign
    for r in board:
        print(f'| {" | ".join(r)} |')


def checking_for_winner(board, sign_to_check, r, c):
    current_row = []
    current_column = []
    left_diagonal = [board[0][0], board[1][1], board[2][2]]
    right_diagonal = [board[0][2], board[1][1], board[2][0]]
    sequence_to_search = [sign_to_check] * 3

    current_row = board[r]

    for row in board:
        current_column.append(row[c])

    if sequence_to_search == current_row or sequence_to_search == current_column or sequence_to_search == left_diagonal or sequence_to_search == right_diagonal:
        return True
    else:
        return False


def play(board):
    winner_name=''
    round_num = 1
    found_winner = False
    players = get_player_info()
    numeration_of_board()
    keys = []
    for key in players:
        keys.append(key)

    first_player_name = keys[0]
    second_player_name = keys[1]

    print(f'{first_player_name} starts first!')

    while not found_winner:
        turn = turns(round_num, first_player_name, second_player_name)
        player_choice = get_player_choice(turn)
        row, column = get_position(player_choice)
        apply_players_choice(board, row, column, players[turn])
        found_winner = checking_for_winner(board, players[turn], row, column)
        if found_winner:
            winner_name=turn
        round_num += 1

    print(f'{winner_name} won!')


play_board = [[' ', ' ', ' '] for _ in range(3)]

play(play_board)
