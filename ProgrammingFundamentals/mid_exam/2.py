biscuits = input().split(', ')
command = input()

while not command == 'No More Money':
    splited_command = command.split()
    if splited_command[0] == 'OutOfStock':
        for i in range(len(biscuits)):
            if biscuits[i] == splited_command[1]:
                biscuits[i] = None
    elif splited_command[0] == 'Required':
        if 0 <= int(splited_command[2]) < len(biscuits) and not biscuits[int(splited_command[2])] == None:
            biscuits[int(splited_command[2])] = splited_command[1]
    elif splited_command[0] == 'Last':
        biscuits.append(splited_command[1])
    command = input()

left_biscuits = [el for el in biscuits if not el == None]

print(' '.join(left_biscuits))
