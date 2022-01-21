rows_columns = int(input())

matrix = [[el for el in input()] for i in range(rows_columns)]

symbol_to_search = input()
found = False

row = 0
col = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == symbol_to_search:
            found = True
            row = i
            col = j
            break
    if found:
        break

if found:
    print(f'({row}, {col})')
else:
    print(f'{symbol_to_search} does not occur in the matrix')
