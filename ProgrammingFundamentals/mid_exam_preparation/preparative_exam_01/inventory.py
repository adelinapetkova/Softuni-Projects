items = input().split(', ')
command = input()

while not command == 'Craft!':
    splited_command = command.split(' - ')
    if splited_command[0] == 'Collect':
        item_count = items.count(splited_command[1])
        if item_count == 0:
            items.append(splited_command[1])
    elif splited_command[0] == 'Drop':
        if splited_command[1] in items:
            items.remove(splited_command[1])
    elif splited_command[0] == 'Combine Items':
        old_new_item = splited_command[1].split(':')
        old_item = old_new_item[0]
        new_item = old_new_item[1]
        if old_item in items:
            items.insert(items.index(old_item) + 1, new_item)
    elif splited_command[0] == 'Renew':
        if splited_command[1] in items:
            items.remove(splited_command[1])
            items.append(splited_command[1])
    command = input()

print(', '.join(items))
