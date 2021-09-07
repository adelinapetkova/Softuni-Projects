factor=int(input())
count=int(input())

list=[]
new_number=0

while len(list)<count:
    new_number+=factor
    list.append(new_number)

print(list)