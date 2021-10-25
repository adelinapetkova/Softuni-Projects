import re

text = input()
regex=r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
valid_names = re.findall(regex, text)
print(' '.join(valid_names))
