def valid_indices_check(row, column):
    if 0 <= row < len(matrix) and 0 <= column < len(matrix[row]):
        return True
    else:
        return False


n = int(input())

matrix = [[int(el) for el in input().split()] for i in range(n)]

while True:
    command = input()
    if command == 'END':
        break
    action, row, column, value = command.split()
    row = int(row)
    column = int(column)
    value = int(value)
    if action == 'Add' and valid_indices_check(row, column):
        matrix[row][column] += value
    elif action == 'Subtract' and valid_indices_check(row, column):
        matrix[row][column] -= value
    else:
        print('Invalid coordinates')

for el in matrix:
    el=[str(num) for num in el]
    print(' '.join(el))

