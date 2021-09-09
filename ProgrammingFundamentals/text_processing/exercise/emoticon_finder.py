text=input()

for i in range(len(text)):
    if text[i]==':':
        result=text[i]+text[i+1]
        print(result)
