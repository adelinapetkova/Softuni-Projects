shopping_list=input().split('!')
command=input()

while not command=='Go Shopping!':
    splited_command=command.split()
    if splited_command[0]=='Urgent':
        if not splited_command[1] in shopping_list:
            shopping_list.insert(0,splited_command[1])
    elif splited_command[0]=='Unnecessary':
        if splited_command[1] in shopping_list:
            shopping_list.remove(splited_command[1])
    elif splited_command[0]=='Correct':
        if splited_command[1] in shopping_list:
            index=shopping_list.index(splited_command[1])
            shopping_list.remove(splited_command[1])
            shopping_list.insert(index,splited_command[2])
    elif splited_command[0]=='Rearrange':
        if splited_command[1] in shopping_list:
            shopping_list.remove(splited_command[1])
            shopping_list.append(splited_command[1])
    command=input()

print(', '.join(shopping_list))