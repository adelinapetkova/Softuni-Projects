def indices_validator(row, column):
    if 0<=row<len(matrix) and 0<=column<len(matrix):
        return True
    return False

size=int(input())

matrix=[[el for el in input().split()] for _ in range(size)]

alice_row=0
alice_col=0
for r in range(size):
    for c in range(size):
        if matrix[r][c]=='A':
            alice_col=c
            alice_row=r
            break

teabags=0
enough_teabags=False
while True:
    if teabags>=10:
        enough_teabags=True
        break
    direction=input()
    matrix[alice_row][alice_col] = '*'
    if direction=='up' and indices_validator(alice_row-1, alice_col):
        alice_row-=1
        if matrix[alice_row][alice_col]=='R':
            matrix[alice_row][alice_col] = '*'
            break
        elif matrix[alice_row][alice_col].isdigit():
            teabags+=int(matrix[alice_row][alice_col])
        matrix[alice_row][alice_col]='*'
    elif direction=='down' and indices_validator(alice_row+1,alice_col):
        alice_row+=1
        if matrix[alice_row][alice_col]=='R':
            matrix[alice_row][alice_col] = '*'
            break
        elif matrix[alice_row][alice_col].isdigit():
            teabags+=int(matrix[alice_row][alice_col])
        matrix[alice_row][alice_col]='*'
    elif direction=='left' and indices_validator(alice_row, alice_col-1):
        alice_col-=1
        if matrix[alice_row][alice_col]=='R':
            matrix[alice_row][alice_col] = '*'
            break
        elif matrix[alice_row][alice_col].isdigit():
            teabags+=int(matrix[alice_row][alice_col])
        matrix[alice_row][alice_col]='*'
    elif direction=='right' and indices_validator(alice_row, alice_col+1):
        alice_col+=1
        if matrix[alice_row][alice_col]=='R':
            matrix[alice_row][alice_col] = '*'
            break
        elif matrix[alice_row][alice_col].isdigit():
            teabags+=int(matrix[alice_row][alice_col])
        matrix[alice_row][alice_col]='*'
    else:
        break


if enough_teabags:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")

for el in matrix:
    print(' '.join(el))