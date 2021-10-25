health=100
bitcoins=0
rooms=input().split('|')
died=False

for el in rooms:
    room=el.split()
    if room[0]=='potion':
        needed_health=100-health
        if int(room[1])<=needed_health:
            health+=int(room[1])
            print(f'You healed for {int(room[1])} hp.')
        else:
            health=100
            print(f'You healed for {needed_health} hp.')
        print(f'Current health: {health} hp.')
    elif room[0]=='chest':
        bitcoins+=int(room[1])
        print(f'You found {int(room[1])} bitcoins.')
    else:
        if health>int(room[1]):
            health-=int(room[1])
            print(f'You slayed {room[0]}.')
        else:
            died=True
            print(f'You died! Killed by {room[0]}.')
            best_room=rooms.index(el)+1
            print(f'Best room: {best_room}')
            break

if not died:
    print("You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')

