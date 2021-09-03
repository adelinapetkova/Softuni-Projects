n=int(input())
num=1
num_is_bigger_than_n=False

for row in range(1,n+1):
    for column in range(1,row+1):
        if num>n:
            num_is_bigger_than_n=True
            break
        else:
          print(num,end=' ')
          num+=1
    if num_is_bigger_than_n:
        break
    print()