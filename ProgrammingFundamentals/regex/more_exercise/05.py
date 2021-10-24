import re

regex_for_title = r'<title>(?P<title>.+)</title>'
regex_for_text = r'<body>(<[^<>]+>)*(?P<text>.+)+(</[^<>]+>)*</body>'
text = input()

title = re.finditer(regex_for_title, text)
found_title=''
for t in title:
    found_title = t.group('title')

found_text = re.finditer(regex_for_text, text)
raw_text = ''
for ft in found_text:
    raw_text = ft.group('text')

result_text = ''
i = 0
while i < len(raw_text):
    if not raw_text[i] == '<' and not raw_text[i] == '\\':
        result_text += raw_text[i]
    elif raw_text[i] == '<':
        while not raw_text[i] == '>':
            i += 1
        if i+1<len(raw_text) and not raw_text[i+1]==' ':
            result_text+=' '
    else:
        i+=1
    i+=1

print(f'Title: {found_title}')
print(f'Content: {result_text}')