def fill_the_box(height, length, width, *args):
    size=height*length*width
    cubes_left=0
    args=list(args)
    for i in range(len(args)):
        if args[i]=='Finish':
            break
        if int(args[i])<=size:
            size-=int(args[i])
        else:
            args[i]=int(args[i])
            args[i]-=size
            size=0
            cubes_left+=args[i]
            for j in range(i+1, len(args)):
                if args[j]=='Finish':
                    break
                else:
                    args[j]=int(args[j])
                    cubes_left+=args[j]
            break
    if size>0:
        return f'There is free space in the box. You could put {size} more cubes.'
    else:
        return f'No more free space! You have {cubes_left} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, 'Finish'))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, 'Finish'))
print(fill_the_box(10, 10, 10, 40, 'Finish', 2, 15, 30))