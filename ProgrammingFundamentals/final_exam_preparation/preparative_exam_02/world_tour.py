text = input()

command = input()

while not command == 'Travel':
    result = ''
    if 'Add' in command:
        action, index, str_to_add = command.split(':')
        beggining = ''
        end = ''
        if 0 <= int(index) < len(text):
            for i in range(0, len(text)):
                if i < int(index):
                    beggining += text[i]
                else:
                    end += text[i]
            result += beggining
            result += str_to_add
            result += end
            text = result
            print(result)
    elif 'Remove' in command:
        action, start_index, end_index = command.split(':')
        start_index = int(start_index)
        end_index = int(end_index)
        part_to_remove = text[start_index:end_index + 1]
        result = text.replace(part_to_remove, '')
        text = result
        print(result)
    elif 'Switch' in command:
        action, old_str, new_str = command.split(':')
        if old_str in text:
            result = text.replace(old_str, new_str)
            text = result
            print(result)
    command = input()

print(f'Ready for world tour! Planned stops: {text}')
