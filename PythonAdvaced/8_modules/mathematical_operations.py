from math import pow


def mathematical_operations(num1, num2, sign):
    if sign=='/':
        print(f'{num1/num2:.2f}')
    elif sign=='*':
        print(f'{num1 * num2:.2f}')
    elif sign=='-':
        print(f'{num1 - num2:.2f}')
    elif sign=='+':
        print(f'{num1 + num2:.2f}')
    elif sign=='^':
        num2=int(num2)
        print(f'{pow(num1, num2):.2f}')
