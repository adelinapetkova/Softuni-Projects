import re
regex=r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
numbers=input()
valid_numbers=re.finditer(regex, numbers)
for num in valid_numbers:
    print(num.group(), end=' ')