beginning=int(input())
end=int(input())
magical_number=int(input())
combination_count=0
combination_found=False

for first_number in range(beginning,end+1):
    for second_number in range(beginning,end+1):
        combination_count+=1
        if first_number+second_number==magical_number:
            combination_found=True
            print(f'Combination N:{combination_count} ({first_number} + {second_number} = {magical_number})')
            break
    if combination_found==True:
        break

if combination_found==False:
    print(f'{combination_count} combinations - neither equals {magical_number}')
