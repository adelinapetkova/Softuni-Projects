import sys

n=input()
min=sys.maxsize

while n!='Stop':
    if int(n)<min:
        min=int(n)
    n = input()

print(min)