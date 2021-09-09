usernames = input().split(', ')

for name in usernames:
    name_is_valid = True
    if 3 <= len(name) <= 16:
        for char in name:
            if not char.isalpha() and not char.isdigit() and not char == '-' and not char == '_':
                name_is_valid = False
                break
            else:
                name_is_valid = True
        if name_is_valid:
            print(name)
    else:
        continue
