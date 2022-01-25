def valid_indices_check(matrix, row, column):
    if row<0 or column<0 or row>=len(matrix) or column>=len(matrix):
        return False
    return matrix[row][column]=='K'


def number_of_hit_knights(matrix, r, c):
    result = 0
    if valid_indices_check(matrix, r - 2, c - 1):
        result += 1
    if valid_indices_check(matrix, r - 2, c + 1):
        result += 1
    if valid_indices_check(matrix, r - 1, c - 2):
        result += 1
    if valid_indices_check(matrix, r - 1, c + 2):
        result += 1
    if valid_indices_check(matrix, r + 1, c - 2):
        result += 1
    if valid_indices_check(matrix, r + 1, c + 2):
        result += 1
    if valid_indices_check(matrix, r + 2, c - 1):
        result += 1
    if valid_indices_check(matrix, r + 2, c + 1):
        result += 1
    return result


n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

removed_knights = 0

while True:
    max_count, row_index, column_index = 0, 0, 0
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == '0':
                continue
            current_count = number_of_hit_knights(matrix, r, c)
            if current_count>max_count:
                max_count=current_count
                row_index=r
                column_index=c
    if max_count==0:
        break
    matrix[row_index][column_index]='0'
    removed_knights+=1

print(removed_knights)
