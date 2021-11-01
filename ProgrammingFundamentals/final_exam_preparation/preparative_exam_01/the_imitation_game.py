encrypted_message = input()

command = input()

while not command == 'Decode':
    split_command = command.split('|')
    if split_command[0] == 'Move':
        num_of_letters_to_move = int(split_command[1])
        letters_to_move = ''
        for i in range(num_of_letters_to_move):
            letters_to_move += encrypted_message[i]
        encrypted_message=encrypted_message.replace(letters_to_move, '')
        encrypted_message += letters_to_move
    elif split_command[0] == 'Insert':
        inserting_index=int(split_command[1])
        symbol_to_insert=split_command[2]
        result=''
        for i in range(inserting_index):
            result+=encrypted_message[i]
        result+=symbol_to_insert
        for j in range(inserting_index,len(encrypted_message)):
            result+=encrypted_message[j]
        encrypted_message=result
    elif split_command[0] == 'ChangeAll':
        char_to_replace=split_command[1]
        replacing_char=split_command[2]
        encrypted_message=encrypted_message.replace(char_to_replace,replacing_char)
    command=input()

print(f'The decrypted message is: {encrypted_message}')