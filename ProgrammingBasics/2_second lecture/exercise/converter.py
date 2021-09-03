number=float(input())
convert_from=input()
convert_to=input()

from_to=f'{convert_from}:{convert_to}'

if from_to=='m:mm':
    result=number*1000
elif from_to=='m:cm':
    result=number*100
elif from_to=='mm:m':
    result=number/1000
elif from_to=='mm:cm':
    result=number/10
elif from_to=='cm:m':
    result=number/100
elif from_to=='cm:mm':
    result=number*10

print(f'{result:.3f}')