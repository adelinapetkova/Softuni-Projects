energy=int(input())
command=input()
count=0
lost=False

while not command=='End of battle':
    distance=int(command)
    if energy<distance:
        print(f'Not enough energy! Game ends with {count} won battles and {energy} energy')
        lost=True
        break
    else:
        energy-=distance
        count+=1
        if count%3==0:
            energy+=count
    command=input()

if not lost:
    print(f'Won battles: {count}. Energy left: {energy}')