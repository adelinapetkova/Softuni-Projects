import sys

n=int(input())

sum=0
diff=0
max=-sys.maxsize

for i in range(n):
    number=int(input())
    sum += number
    if number>max:
        max=number

sum=sum-max
if max == sum:
    print('Yes')
    print(f'Sum = {sum}')
else:
    diff = abs(sum - max)
    print('No')
    print(f'Diff = {diff}')



