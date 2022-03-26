board = [[el for el in input().split()] for _ in range(8)]

capturing_queens = []
queens=[]
king_row = 0
king_column = 0

for r in range(8):
    for c in range(8):
        if board[r][c]=='K':
            king_column=c
            king_row=r

sequences=[]

up = []
for row in range(king_row - 1, -1, -1):
    up.append([row,king_column])

down = []
for row in range(king_row + 1, 8):
    down.append([row,king_column])

left = []
for col in range(king_column - 1, -1, -1):
    left.append([king_row,col])

right = []
for col in range(king_column + 1, 8):
    right.append([king_row,col])

left_upper_diagonal = []
row = king_row
col = king_column
while row > 0 and col > 0:
    row -= 1
    col -= 1
    left_upper_diagonal.append([row,col])

right_down_diagonal = []
row = king_row
col = king_column
while row < 7 and col < 7:
    row += 1
    col += 1
    right_down_diagonal.append([row,col])

right_upper_diagonal = []
row = king_row
col = king_column
while 0 < row < 7 and 0 < col < 7:
    row -= 1
    col += 1
    right_upper_diagonal.append([row,col])

left_down_diagonal = []
row = king_row
col = king_column
while 0 < row < 7 and 0 < col < 7:
    row += 1
    col -= 1
    left_down_diagonal.append([row,col])

sequences.append(left)
sequences.append(right)
sequences.append(up)
sequences.append(down)
sequences.append(left_upper_diagonal)
sequences.append(left_down_diagonal)
sequences.append(right_upper_diagonal)
sequences.append(right_down_diagonal)


for el in sequences:
    for position in el:
        row=position[0]
        col=position[1]
        if board[row][col]=='Q':
            capturing_queens.append(position)
            break


if capturing_queens:
    for el in capturing_queens:
        print(el)
else:
    print('The king is safe!')


