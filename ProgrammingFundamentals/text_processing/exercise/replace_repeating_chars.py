text = input()
result=''

for i in range(len(text)):
    if i == 0:
        result+=text[i]
        continue
    else:
        previous_char = text[i - 1]
        char = text[i]
        if not char==previous_char:
            result+=char

print(result)

