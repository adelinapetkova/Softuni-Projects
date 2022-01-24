def indices_validator(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


num_of_presents = int(input())
size = int(input())

matrix = [[el for el in input().split()] for _ in range(size)]

santa_row = 0
santa_col = 0
nice_kids = 0

for r in range(size):
    for c in range(size):
        if matrix[r][c] == 'S':
            santa_col = c
            santa_row = r
        elif matrix[r][c] == 'V':
            nice_kids += 1

given_presents_to_nice_kids = 0

while num_of_presents > 0:
    valid = False
    command = input()
    if command == 'Christmas morning':
        break
    elif command == 'up' and indices_validator(santa_row - 1, santa_col, size):
        matrix[santa_row][santa_col] = '-'
        santa_row -= 1
        valid = True
    elif command == 'down' and indices_validator(santa_row + 1, santa_col, size):
        matrix[santa_row][santa_col] = '-'
        santa_row += 1
        valid = True
    elif command == 'left' and indices_validator(santa_row, santa_col - 1, size):
        matrix[santa_row][santa_col] = '-'
        santa_col -= 1
        valid = True
    elif command == 'right' and indices_validator(santa_row, santa_col + 1, size):
        matrix[santa_row][santa_col] = '-'
        santa_col += 1
        valid = True

    if valid:
        if matrix[santa_row][santa_col] == 'V':
            num_of_presents -= 1
            given_presents_to_nice_kids += 1
            matrix[santa_row][santa_col] = '-'
        elif matrix[santa_row][santa_col] == 'C':
            if matrix[santa_row - 1][santa_col] == 'X':
                num_of_presents -= 1
                matrix[santa_row - 1][santa_col] = '-'
            elif matrix[santa_row - 1][santa_col] == 'V':
                num_of_presents -= 1
                given_presents_to_nice_kids += 1
                matrix[santa_row - 1][santa_col] = '-'

            if num_of_presents == 0:
                break

            if matrix[santa_row + 1][santa_col] == 'X':
                num_of_presents -= 1
                matrix[santa_row + 1][santa_col] = '-'
            elif matrix[santa_row + 1][santa_col] == 'V':
                num_of_presents -= 1
                given_presents_to_nice_kids += 1
                matrix[santa_row + 1][santa_col] = '-'

            if num_of_presents == 0:
                break

            if matrix[santa_row][santa_col - 1] == 'X':
                num_of_presents -= 1
                matrix[santa_row][santa_col - 1] = '-'
            elif matrix[santa_row][santa_col - 1] == 'V':
                num_of_presents -= 1
                given_presents_to_nice_kids += 1
                matrix[santa_row][santa_col - 1] = '-'

            if num_of_presents == 0:
                break

            if matrix[santa_row][santa_col + 1] == 'X':
                num_of_presents -= 1
                matrix[santa_row][santa_col + 1] = '-'
            elif matrix[santa_row][santa_col + 1] == 'V':
                num_of_presents -= 1
                given_presents_to_nice_kids += 1
                matrix[santa_row][santa_col + 1] = '-'

        matrix[santa_row][santa_col] = 'S'

if num_of_presents == 0:
    if given_presents_to_nice_kids < nice_kids:
        print('Santa ran out of presents!')

for el in matrix:
    print(' '.join(el))

if given_presents_to_nice_kids == nice_kids:
    print(f'Good job, Santa! {nice_kids} happy nice kid/s.')
else:
    nice_kids_without_present = nice_kids - given_presents_to_nice_kids
    print(f'No presents for {nice_kids_without_present} nice kid/s.')
