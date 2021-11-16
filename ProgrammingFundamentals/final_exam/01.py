name=input()
command=input()

while not command=='Sign up':
    if 'Case' in command:
        action, case=command.split()
        if case=='lower':
            name=name.lower()
            print(name)
        else:
            name=name.upper()
            print(name)
    elif 'Reverse' in command:
        action, start_index, end_index=command.split()
        start_index=int(start_index)
        end_index=int(end_index)
        if 0<=start_index<len(name) and 0<=end_index<len(name):
            substring=name[start_index:end_index+1]
            print(substring[::-1])
    elif 'Cut' in command:
        action, substring=command.split()
        if substring in name:
            name=name.replace(substring, '')
            print(name)
        else:
            print(f"The word {name} doesn't contain {substring}.")
    elif 'Replace' in command:
        action, char_to_replace=command.split()
        name=name.replace(char_to_replace, '*')
        print(name)
    elif 'Check' in command:
        action, char_to_check=command.split()
        if char_to_check in name:
            print('Valid')
        else:
            print(f'Your username must contain {char_to_check}.')
    command=input()