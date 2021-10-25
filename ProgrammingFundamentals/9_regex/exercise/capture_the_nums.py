import re

text=''
while True:
    a=input()
    if a:
        text+=a
        text+=' '
    else:
        break
regex=r'\d+'
nums=re.findall(regex, text)
print(*nums)
