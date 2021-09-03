sum=0
money_input=input()

while money_input!='NoMoreMoney':
    if float(money_input) < 0:
        print('Invalid operation!')
        break
    else:
       print(f'Increase: {float(money_input):.2f}')
       sum+=float(money_input)
       money_input=input()

print(f'Total: {sum:.2f}')

