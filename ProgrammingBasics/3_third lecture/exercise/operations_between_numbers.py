n1=int(input())
n2=int(input())
operation=input()

result=0

if operation=='+' or operation=='*' or operation=='-':
    if operation=='+':
        result=n2+n1
    elif operation=='*':
        result=n2*n1
    elif operation=='-':
        result=n1-n2
    if result%2==0:
        e_o='even'
    else:
        e_o='odd'
    print(f'{n1} {operation} {n2} = {result} - {e_o}')
elif operation=='/':
    if n2!=0:
       result=n1/n2
       print(f'{n1} / {n2} = {result:.2f}')
    else:
        print(f'Cannot divide {n1} by zero')
elif operation=='%':
    if n2!=0:
        result=n1%n2
        print(f'{n1} % {n2} = {result}')
    else:
        print(f'Cannot divide {n1} by zero')

