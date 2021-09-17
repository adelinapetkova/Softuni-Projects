import re

text = input()
searched_word = input()
regex = fr'\b{searched_word}\b'
found = re.findall(regex, text, flags=re.IGNORECASE)
print(len(found))
