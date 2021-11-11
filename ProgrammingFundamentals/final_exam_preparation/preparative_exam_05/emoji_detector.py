import re

text=input()
digits_in_text=re.findall(r'\d', text)
cool_threshold=1
for digit in digits_in_text:
    cool_threshold=cool_threshold*int(digit)
print(f'Cool threshold: {cool_threshold}')
regex_for_emojis=r'(?P<sep>[:|*]){2}(?P<emoji>[A-Z][a-z]{2,})(?P=sep){2}'

valid_emojis=re.finditer(regex_for_emojis, text)
cool_emojis=[]
i=0

for emoji in valid_emojis:
    i+=1
    sum_of_asciis=0
    for char in emoji.group('emoji'):
        sum_of_asciis+=ord(char)
    if sum_of_asciis>cool_threshold:
        cool_emojis.append(emoji.group())

print(f'{i} emojis found in the text. The cool ones are:')
for e in cool_emojis:
    print(e)