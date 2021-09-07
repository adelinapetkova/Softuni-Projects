number_1=int(input())
number_2=int(input())

def factorial_division(num_1,num_2):
    first_result = 1
    second_result=1
    for i in range(1,num_1+1):
        first_result=first_result*i
    for j in range(1,num_2+1):
        second_result=second_result*j
    result=first_result/second_result
    return f'{result:.2f}'

print(factorial_division(number_1,number_2))