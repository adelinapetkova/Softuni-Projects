number=input()

def odd_even_sum(num_as_string):
    even_sum = 0
    odd_sum = 0
    for digit in num_as_string:
        if int(digit)%2==0:
            even_sum+=int(digit)
        else:
            odd_sum+=int(digit)
    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')


odd_even_sum(number)