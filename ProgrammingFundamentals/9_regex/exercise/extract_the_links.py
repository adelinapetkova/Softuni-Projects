import re
regex=r'(www\.[a-zA-Z0-9]+(\-[a-zA-Z0-9]+)*\.[a-z]+((\.[a-z]+)+)?)'

sentence=input()
valid_links=[]

while not sentence=='':
    valid_links_matches=re.finditer(regex, sentence)
    for link in valid_links_matches:
        valid_links.append(link.group())
    sentence=input()

for i in valid_links:
    print(i)


