n=int(input())

total=0
total1=0

for i in range(n):
    number=int(input())
    total+=number

for i in range(n):
    number=int(input())
    total1+=number

if total==total1:
    print(f'Yes, sum = {total1}')
elif total<total1 or total>total1:
    difference=abs(total-total1)
    print(f'No, diff = {difference}')
