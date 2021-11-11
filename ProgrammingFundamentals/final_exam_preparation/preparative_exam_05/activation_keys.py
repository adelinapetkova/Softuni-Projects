activation_key=input()

command=input()

while not command=='Generate':
    if 'Contains' in command:
        action, substring=command.split('>>>')
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif 'Flip' in command:
        action, case, start_index, end_index=command.split('>>>')
        start_index=int(start_index)
        end_index=int(end_index)
        substring_to_change=activation_key[start_index:end_index]
        if case=='Upper':
            activation_key=activation_key.replace(substring_to_change, substring_to_change.upper())
        else:
            activation_key=activation_key.replace(substring_to_change, substring_to_change.lower())
        print(activation_key)
    elif 'Slice' in command:
        action, start_index, end_index=command.split('>>>')
        start_index=int(start_index)
        end_index=int(end_index)
        substring_to_remove=activation_key[start_index:end_index]
        activation_key=activation_key.replace(substring_to_remove, '')
        print(activation_key)
    command=input()

print(f'Your activation key is: {activation_key}')