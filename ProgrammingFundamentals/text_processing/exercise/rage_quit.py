text=input()
repeating_times=''
text_to_repeat=''
result=''
unique_symbols=[]

for i in range(len(text)):
    if text[i].isdigit():
        repeating_times+=text[i]
        if i+1<len(text) and text[i+1].isdigit():
            repeating_times+=text[i+1]
        result+=text_to_repeat.upper()*int(repeating_times)
        repeating_times = ''
        text_to_repeat = ''
    else:
        text_to_repeat+=text[i]
        if text[i].lower() not in unique_symbols:
            unique_symbols.append(text[i].lower())

print(f'Unique symbols used: {len(unique_symbols)}')
print(result)