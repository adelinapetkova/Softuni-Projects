k=int(input())
l=int(input())
m=int(input())
n=int(input())
turns=0
first_number=''
second_number=''
a=0
while turns<6:
    a+=1
    if a==2:
        break
    if turns == 6:
        break
    for i in range(k,9):
        if turns == 6:
            break
        for j in range(9,l-1,-1):
            if turns == 6:
                break
            for p in range(m, 9):
                if turns == 6:
                    break
                for q in range(9, n-1,-1):
                    first_number = ''
                    second_number = ''
                    if i%2==0 and j%2==1:
                        first_number+=str(i)
                        first_number+=str(j)
                    if p % 2 == 0 and q % 2 == 1:
                        second_number += str(p)
                        second_number += str(q)
                    if first_number!='' and second_number!='':
                        if first_number == second_number:
                            print('Cannot change the same player.')
                        else:
                            print(f'{int(first_number)} - {int(second_number)}')
                            turns += 1
                    if turns==6:
                        break


