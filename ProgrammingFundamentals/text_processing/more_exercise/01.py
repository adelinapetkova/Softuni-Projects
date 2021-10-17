n=int(input())

for i in range(n):
    text=input()
    name_found=False
    age_found=False
    name=''
    age=''
    for el in text:
        if el=='|':
            name_found=False
        if el=='*':
            age_found=False
        if el=='@':
            name_found=True
        elif name_found:
            name+=el
        if el=='#':
            age_found=True
        elif age_found:
            age+=el
    print(f'{name} is {age} years old.')