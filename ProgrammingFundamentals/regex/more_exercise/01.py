import re

competitors = input().split(', ')
text = input()
regex_for_letters = r'[a-zA-Z]+'
regex_for_digits = r'\d'
distances = {}

while not text == 'end of race':
    letters = re.findall(regex_for_letters, text)
    digits = [int(el) for el in re.findall(regex_for_digits, text)]
    name = ''.join(letters)
    distance = sum(digits)
    if name in competitors:
        if name not in distances:
            distances[name] = distance
        else:
            distances[name] += distance
    text = input()

a = dict(sorted(distances.items(), key=lambda x: (-x[1])))


winners=[]
i=1
for key in a:
    if i>3:
        break
    winners.append(key)

print(f'1st place: {winners[0]}')
print(f'2nd place: {winners[1]}')
print(f'3rd place: {winners[2]}')

