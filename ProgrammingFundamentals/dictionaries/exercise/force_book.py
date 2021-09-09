command = input()
sides_and_users = {}

while not command == 'Lumpawaroo':
    if '|' in command:
        side, user = command.split(' | ')
        user_found = False
        for value in sides_and_users.values():
            if user in value:
                user_found = True
        if side not in sides_and_users and not user_found:
            sides_and_users[side] = []
            sides_and_users[side].append(user)
        elif not user_found:
            sides_and_users[side].append(user)
        elif user_found:
            command = input()
            continue
    elif '->' in command:
        user, side = command.split(' -> ')
        user_found = False
        for value in sides_and_users.values():
            if user in value:
                user_found = True
        if user_found:
            for key, value in sides_and_users.items():
                if user in value:
                    sides_and_users[key].remove(user)
            sides_and_users[side].append(user)
        elif not user_found and side not in sides_and_users:
            sides_and_users[side] = []
            sides_and_users[side].append(user)
        elif not user_found:
            sides_and_users[side].append(user)

        print(f'{user} joins the {side} side!')
    command = input()

sorted_dictionary = dict(sorted(sides_and_users.items(), key=lambda x: (-len(x[1]), x[0])))

for key, value in sorted_dictionary.items():
    if not len(value) == 0:
        print(f'Side: {key}, Members: {len(value)}')
        sorted_value = list(sorted(value))
        for el in sorted_value:
            print(f'! {el}')
