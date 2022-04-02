size=6

board=[[el for el in input().split()] for _ in range(size)]
points=0

for i in range(3):
    throw=input()
    coordinates=[]
    for el in throw:
        if el.isdigit():
            coordinates.append(int(el))
    row=coordinates[0]
    column=coordinates[1]

    if not (0<=row<size and 0<=column<size):
        continue

    if board[row][column]=='B':
        for r in range(0,size):
            if board[r][column].isdigit():
                points+=int(board[r][column])

        board[row][column]='0'


prize=''

if 100<=points<=199:
    prize='Football'
elif 200<=points<=299:
    prize='Teddy Bear'
elif points>=300:
    prize='Lego Construction Set'

needed_points=0
if prize=='':
    needed_points=100-points

if not prize=='':
    print(f"Good job! You scored {points} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {needed_points} points more to win a prize.")
