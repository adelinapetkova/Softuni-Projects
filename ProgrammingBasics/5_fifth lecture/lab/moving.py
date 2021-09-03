width=int(input())
length=int(input())
height=int(input())

volume_of_room=width*length*height
volume_of_a_box=1
number_of_boxes_in_room=volume_of_room
command=input()
boxes=0

while command!='Done':
    boxes+=int(command)
    if boxes>number_of_boxes_in_room:
        break
    command=input()

if boxes<=number_of_boxes_in_room:
    left=number_of_boxes_in_room-boxes
    print(f'{left} Cubic meters left.')
else:
    needed_space=boxes-number_of_boxes_in_room
    print(f'No more free space! You need {needed_space} Cubic meters more.')

