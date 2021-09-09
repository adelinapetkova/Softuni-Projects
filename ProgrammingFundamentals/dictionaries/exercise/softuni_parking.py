n=int(input())
parking_lot={}

for _ in range(n):
    command=input().split()
    if command[0]=='register':
        if command[1] not in parking_lot:
            parking_lot[command[1]]=command[2]
            print(f'{command[1]} registered {command[2]} successfully')
        else:
            print(f'ERROR: already registered with plate number {parking_lot[command[1]]}')
    else:
        if command[1] not in parking_lot:
            print(f'ERROR: user {command[1]} not found')
        else:
            parking_lot.pop(command[1])
            print(f'{command[1]} unregistered successfully')

for key, value in parking_lot.items():
    print(f'{key} => {value}')