number = input()
prime_sum = 0
nonprime_sum = 0

while number != 'stop':
    is_prime = True
    if int(number) < 0:
        print('Number is negative.')
    else:
        for divide in range(2, int(number)):
            if int(number) % divide == 0:
                is_prime = False
                break
        if is_prime == False:
            nonprime_sum += int(number)
        else:
            prime_sum += int(number)
    number = input()

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {nonprime_sum}')
