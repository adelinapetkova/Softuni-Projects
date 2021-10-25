import re
regex=r'(?<=\b_)[a-zA-Z0-9]+\b'
valid=re.finditer(regex,input())

valid_words=[]
for word in valid:
    valid_words.append(word.group())

print(','.join(valid_words))