def get_primes(integers):
    for x in integers:
        divisors = 0
        for i in range(1, x + 1):
            if x % i == 0:
                divisors += 1
        if divisors==2:
            yield x


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

print(list(get_primes([-1, 0, 0, 1, 1, 0])))