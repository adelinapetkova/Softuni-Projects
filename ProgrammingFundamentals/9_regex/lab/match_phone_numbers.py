import re

numbers = input()
regex = r'(\+359 2 \d{3} \d{4})|(\+359-2-\d{3}-\d{4})'
valid_numbers = re.finditer(regex, numbers)

valid_phones=[phone.group() for phone in valid_numbers]
print(', '.join(valid_phones))
