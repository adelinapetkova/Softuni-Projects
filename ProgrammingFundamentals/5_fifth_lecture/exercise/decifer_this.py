words = input().split()

for word in words:
    first_letter = ''
    string = []
    for el in word:
        if 48 <= ord(el) <= 57:
            first_letter += el
        else:
            string.append(el)
    string.insert(0, chr(int(first_letter)))
    string[1], string[len(string) - 1] = string[len(string) - 1], string[1]
    print(''.join(string), end=' ')
