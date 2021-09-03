import sys

n=input()
max=-sys.maxsize

while n!='Stop':
    if int(n)>max:
        max=int(n)
    n = input()

print(max)