number_of_tabs=int(input())
salary=int(input())

for i in range(number_of_tabs):
    tab=input()
    if tab=='Facebook':
        salary-=150
    elif tab=='Instagram':
        salary-=100
    elif tab=='Reddit':
        salary-=50
    if salary==0:
        print('You have lost your salary.')
        break
if salary!=0:
   print(salary)