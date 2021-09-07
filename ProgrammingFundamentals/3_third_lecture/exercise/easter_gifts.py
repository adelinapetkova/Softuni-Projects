gifts=input().split()
command=input().split()

while not command==['No', 'Money']:
    if command[0]=='OutOfStock':
        for i in range(len(gifts)):
            if gifts[i]==command[1]:
                gifts[i]='None'
    elif command[0]=='Required':
        if int(command[2]) in range(len(gifts)):
           gifts[int(command[2])]=command[1]
    elif command[0]=='JustInCase':
        gifts[len(gifts)-1]=command[1]
    command=input().split()

for gift in gifts:
    if not gift=='None':
        print(gift,end=' ')

