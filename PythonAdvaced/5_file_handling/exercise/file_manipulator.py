import os
from os import path

while True:
    command=input()
    if command=='End':
        break
    elif 'Create' in command:
        action, file_name=command.split('-')
        file=open(file_name, 'w').close()
    elif 'Add' in command:
        action, file_name, content=command.split('-')
        file=open(file_name, 'a')
        file.write(f'{content}\n')
        file.close()
    elif 'Replace' in command:
        action, file_name, old_string, new_string=command.split('-')
        if os.path.exists(file_name):
            with open(file_name, 'r+') as file:
                content=file.read().replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(content)
        else:
            print('An error occurred')
    elif 'Delete' in command:
        action, file_name=command.split('-')
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print('An error occurred')

