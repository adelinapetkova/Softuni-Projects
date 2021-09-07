version=input().split('.')
num1=int(version[0])
num2=int(version[1])
num3=int(version[2])

def upgrade_version(n1,n2,n3):
    if n3==9:
        n3=0
        if n2==9:
            n2=0
            n1+=1
        else:
            n2+=1
    else:
        n3+=1
    print(f'{n1}.{n2}.{n3}')

upgrade_version(num1,num2,num3)
