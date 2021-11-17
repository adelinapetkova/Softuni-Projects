text=input()

characters=[]

for ch in text:
    characters.append(ch)

result=''

while len(characters)>0:
    result+=characters.pop()

print(result)