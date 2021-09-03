movie=input()
student_tickets=0
kid_tickets=0
standart_tickets=0
tickets=0
total_tickets=0

while movie!='Finish':
    seats=int(input())
    for ticket in range(1,seats+1):
        type_of_ticket=input()
        if type_of_ticket=='End':
            break
        elif type_of_ticket=='student':
            student_tickets+=1
        elif type_of_ticket=='standard':
            standart_tickets+=1
        elif type_of_ticket=='kid':
            kid_tickets+=1
        tickets=ticket
    total_tickets+=tickets
    fullness=(tickets/seats)*100
    print(f'{movie} - {fullness:.2f}% full.')
    movie=input()

student_percentage=(student_tickets/total_tickets)*100
standart_percentage=(standart_tickets/total_tickets)*100
kid_percentage=(kid_tickets/total_tickets)*100

print(f'Total tickets: {total_tickets}')
print(f'{student_percentage:.2f}% student tickets.')
print(f'{standart_percentage:.2f}% standard tickets.')
print(f'{kid_percentage:.2f}% kids tickets.')