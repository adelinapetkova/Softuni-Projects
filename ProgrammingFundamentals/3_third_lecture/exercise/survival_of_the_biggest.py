import sys

integers_list=input().split()
n=int(input())

for i in range(n):
    minimal_number = sys.maxsize
    for element in integers_list:
        if int(element)<minimal_number:
            minimal_number=int(element)
    integers_list.remove(str(minimal_number))

m=0
for number in integers_list:
    m+=1
    if m==len(integers_list):
        print(int(number))
    else:
        print(f'{int(number)}, ',end='')
