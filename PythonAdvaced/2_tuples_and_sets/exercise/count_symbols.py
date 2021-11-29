text = input()

characters = {}

for ch in text:
    if ch not in characters:
        characters[ch] = 0
    characters[ch] += 1

characters = dict(sorted(characters.items(), key=lambda x: x[0]))

for char, times in characters.items():
    print(f'{char}: {times} time/s')