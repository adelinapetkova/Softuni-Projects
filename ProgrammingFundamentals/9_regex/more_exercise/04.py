import re

regex_for_words = r'[^,\s]+'
text = input()
valid_names = re.findall(regex_for_words, text)
regex_for_health = r'[^0-9+\.*/-]'
regex_for_numbers = r'-?\d+(\.\d+)?'
regex_for_actions = r'\*|/'
demons = {}

for name in valid_names:
    health = 0
    damage = 0
    characters_for_health = re.findall(regex_for_health, name)
    for char in characters_for_health:
        health += ord(char)
    numbers = re.finditer(regex_for_numbers, name)
    for num in numbers:
        damage += float(num.group())
    actions = re.findall(regex_for_actions, name)
    for act in actions:
        if act == '/':
            damage = damage / 2
        else:
            damage = damage * 2
    demons[name] = {}
    demons[name][health] = damage

a = dict(sorted(demons.items(), key=lambda x: x[0]))

for name, value in a.items():
    for health1, damage1 in value.items():
        print(f'{name} - {health1} health, {damage1:.2f} damage')
