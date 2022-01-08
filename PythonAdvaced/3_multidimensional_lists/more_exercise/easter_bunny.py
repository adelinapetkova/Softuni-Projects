size=int(input())

matrix = [[el for el in input().split()] for i in range(size)]

bunny_row=0
bunny_col=0
for r in range(size):
    for c in range(size):
        if matrix[r][c]=='B':
            bunny_col=c
            bunny_row=r
            break

max_eggs=0
steps=[]
direction=''

eggs=0
dire=''
step=[]
for row in range(bunny_row-1, -1, -1):
    dire='up'
    col=bunny_col
    if matrix[row][col]=='X':
        break
    eggs+=int(matrix[row][col])
    step.append([row,col])


if eggs>=max_eggs:
    max_eggs=eggs
    direction=dire
    steps=step


eggs=0
step=[]
for row in range(bunny_row + 1, size):
    dire='down'
    col = bunny_col
    if matrix[row][col] == 'X':
        break
    eggs += int(matrix[row][col])
    step.append([row, col])

if eggs>=max_eggs:
    max_eggs=eggs
    direction=dire
    steps=step


eggs=0
step=[]
for col in range(bunny_col - 1, -1, -1):
    dire = 'left'
    row = bunny_row
    if matrix[row][col] == 'X':
        break
    eggs += int(matrix[row][col])
    step.append([row, col])


if eggs>=max_eggs:
    max_eggs=eggs
    direction=dire
    steps=step

eggs=0
step=[]
for col in range(bunny_col + 1, size):
    dire = 'right'
    row = bunny_row
    if matrix[row][col] == 'X':
        break
    eggs += int(matrix[row][col])
    step.append([row, col])


if eggs>=max_eggs:
    max_eggs=eggs
    direction=dire
    steps=step

print(direction)
for el in steps:
    print(el)
print(max_eggs)