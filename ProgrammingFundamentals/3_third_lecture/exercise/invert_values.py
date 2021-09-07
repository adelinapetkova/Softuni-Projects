list=input().split()
inverted_list=[]

for element in list:
    number=int(element)*-1
    inverted_list.append(number)

print(inverted_list)

