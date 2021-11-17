text = input()

opening_parentheses = []
balanced = True
pairs={
    '(':')',
    '{':'}',
    '[':']',
}

for ch in text:
    if ch in '({[':
        opening_parentheses.append(ch)
    else:
        if len(opening_parentheses)==0:
            balanced=False
            break
        last_opened = opening_parentheses.pop()
        if not pairs[last_opened]==ch:
            balanced=False
            break

if balanced and len(opening_parentheses)==0:
    print('YES')
else:
    print('NO')
