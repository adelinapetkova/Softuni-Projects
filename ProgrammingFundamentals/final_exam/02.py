import re
n=int(input())
regex=r'(?P<sep>.+)>(?P<nums>\d{3})\|(?P<small>[a-z]{3})\|(?P<big>[A-Z]{3})\|(?P<symbols>[^<>]{3})<(?P=sep)'

for _ in range(n):
    is_valid=False
    password=input()
    valid=re.finditer(regex,password)
    for v in valid:
        is_valid=True
        passw=v.group('nums')+v.group('small')+v.group('big')+v.group('symbols')
        print(f'Password: {passw}')
    if not is_valid:
        print('Try another password!')
