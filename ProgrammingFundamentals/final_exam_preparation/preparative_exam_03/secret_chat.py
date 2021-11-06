message = input()

command = input()

while not command == 'Reveal':
    result = ''
    if 'InsertSpace' in command:
        action, index = command.split(':|:')
        index = int(index)
        beginning = ''
        end = ''
        for i in range(len(message)):
            if i < index:
                beginning += message[i]
            else:
                end += message[i]
        result += beginning
        result += ' '
        result += end
        message = result
        print(message)
    elif 'Reverse' in command:
        action, substring = command.split(':|:')
        if substring in message:
            result = message.replace(substring, '', 1)
            reversed_substring = substring[::-1]
            result += reversed_substring
            message = result
            print(message)
        else:
            print('error')
    elif 'ChangeAll' in command:
        action, substring, replacement = command.split(':|:')
        result = message.replace(substring, replacement)
        message = result
        print(message)
    command = input()

print(f'You have a new text message: {message}')
