integers = [int(el) for el in input().split()]
command = input()

while not command == 'end':
    splited_command = command.split()
    if splited_command[0] == 'swap':
        integers[int(splited_command[1])], integers[int(splited_command[2])] = \
            integers[int(splited_command[2])], integers[int(splited_command[1])]
    elif splited_command[0] == 'multiply':
        integers[int(splited_command[1])] = integers[int(splited_command[1])] * integers[int(splited_command[2])]
    elif splited_command[0] == 'decrease':
        for i in range(0, len(integers)):
            integers[i]=integers[i]-1
    command = input()

integers_as_str = [str(el) for el in integers]
print(', '.join(integers_as_str))
