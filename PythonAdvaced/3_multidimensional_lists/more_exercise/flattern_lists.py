strings=input().split('|')
lists=[el.split() for el in strings]

flat_list=[]
for i in range(len(lists)-1, -1, -1):
    for num in lists[i]:
        flat_list.append(num)

print(' '.join(flat_list))