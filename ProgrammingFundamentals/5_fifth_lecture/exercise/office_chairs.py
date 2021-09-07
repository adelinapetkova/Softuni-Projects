rooms=int(input())
free_chairs=0
needed_chairs=0

for room in range(1,rooms+1):
    chairs_and_visitors=input().split()
    chairs=len(chairs_and_visitors[0])
    visitors=int(chairs_and_visitors[1])
    if chairs>visitors:
        free_chairs+=chairs-visitors
    elif chairs<visitors:
        needed_chairs=visitors-chairs
        print(f'{needed_chairs} more chairs needed in room {room}')

if needed_chairs==0:
    print(f'Game On, {free_chairs} free chairs left')