text=input()
result=''
number_of_explosions=0
i=0

while i<len(text):
    current_char=text[i]
    if not current_char=='>':
        result+=current_char
    else:
        result+=current_char
        number_of_explosions+=int(text[i+1])
        while number_of_explosions>0:
            i+=1
            number_of_explosions-=1
            if i>=len(text):
                break
            if text[i]=='>':
                result+=text[i]
                number_of_explosions+=int(text[i+1])
                i+=1
    i+=1

print(result)

