list_10=[0]*10

task=input().split('-')

while not task[0]=='End':
    list_10[int(task[0])-1]=task[1]
    task = input().split('-')

to_do_list=[el for el in list_10 if not el==0]

print(to_do_list)
