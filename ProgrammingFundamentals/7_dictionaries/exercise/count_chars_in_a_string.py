text = input()
chars = {}

for character in text:
    if not character == ' ':
        if character not in chars:
            chars[character] = 1
        else:
            chars[character] += 1

for key, value in chars.items():
    print(f'{key} -> {value}')
