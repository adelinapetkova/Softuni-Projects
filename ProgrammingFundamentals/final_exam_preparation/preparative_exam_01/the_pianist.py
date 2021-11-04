n = int(input())
info = {}

for _ in range(n):
    piece, composer, key = input().split('|')
    info[piece] = {}
    info[piece][composer] = key

command = input()

while not command == 'Stop':
    split_command = command.split('|')
    if split_command[0] == 'Add':
        if split_command[1] not in info:
            info[split_command[1]] = {}
            info[split_command[1]][split_command[2]] = split_command[3]
            print(f"{split_command[1]} by {split_command[2]} in {split_command[3]} added to the collection!")
        else:
            print(f"{split_command[1]} is already in the collection!")
    elif split_command[0] == 'Remove':
        if split_command[1] in info:
            info.pop(split_command[1])
            print(f'Successfully removed {split_command[1]}!')
        else:
            print(f"Invalid operation! {split_command[1]} does not exist in the collection.")
    elif split_command[0] == 'ChangeKey':
        if split_command[1] in info:
            author_key = info[split_command[1]]
            author = ''
            for a in author_key:
                author = a
            info[split_command[1]][author] = split_command[2]
            print(f"Changed the key of {split_command[1]} to {split_command[2]}!")
        else:
            print(f"Invalid operation! {split_command[1]} does not exist in the collection.")
    command = input()

a = dict(sorted(info.items(), key=lambda x: (x[0], x[1])))

for key, value in a.items():
    for key1, value1 in value.items():
        print(f'{key} -> Composer: {key1}, Key: {value1}')
