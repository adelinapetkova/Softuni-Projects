cakes=int(input())
max_points=0
winner=''

for i in range(cakes):
    total_points = 0
    cook=input()
    points=input()
    while points!='Stop':
        total_points+=int(points)
        points=input()
    print(f'{cook} has {total_points} points.')
    if total_points>max_points:
        winner=cook
        max_points=total_points
        print(f'{cook} is the new number 1!')

print(f'{winner} won competition with {max_points} points!')
