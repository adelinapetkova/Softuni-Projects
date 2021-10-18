import re

n=int(input())

attacked=[]
destroyed=[]
num_a=0
num_d=0
regex=r'(?P<planet>(?<=@)[a-zA-Z]+)([^@!>:-]+)?:(?P<population>\d+)([^@!>:-]+)?!(?P<attack>[A-Z])!([^@!>:-]+)?->(?P<soldiers>\d+)'
for _ in range(n):
    text=input()
    lowered_text=text.lower()
    result=''
    number = lowered_text.count('s') + lowered_text.count('t') + lowered_text.count('a') + lowered_text.count('r')
    for symbol in text:
        result+=chr(ord(symbol)-number)
    a=re.finditer(regex, result)
    for planet in a:
        if planet.group('attack')=='A':
            num_a+=1
            attacked.append(planet.group('planet'))
        elif planet.group('attack')=='D':
            num_d+=1
            destroyed.append(planet.group('planet'))

a=list(sorted(attacked))
d=list(sorted(destroyed))
print(f'Attacked planets: {len(attacked)}')
for planet in a:
    print(f'-> {planet}')
print(f'Destroyed planets: {len(destroyed)}')
for pl in d:
    print(f'-> {pl}')