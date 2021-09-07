coins=input().split(', ')
num_of_beggars=int(input())
list=[]

for beggar in range(1,num_of_beggars+1):
    sum_of_coins=0
    for i in range(beggar,len(coins)+1,num_of_beggars):
        sum_of_coins+=int(coins[i-1])
    list.append(sum_of_coins)

print(list)