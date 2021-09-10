import re
text = input()
regex=r'(^|(?<=\s))[a-z0-9]+[\._-]?[a-z0-9]+@([a-z]+[-]?[a-z]+)\.([a-z]+[-]?[a-z]+)(\.[a-z]+[-]?[a-z]+)?'
valid_emails=re.finditer(regex, text)

for email in valid_emails:
    print(email.group())