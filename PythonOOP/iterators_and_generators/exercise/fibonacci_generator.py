def fibonacci():
    first_number = 0
    yield first_number
    second_number = 1
    yield second_number
    while True:
        third_number = first_number + second_number
        yield third_number
        first_number = second_number
        second_number = third_number


generator = fibonacci()
for i in range(1):
    print(next(generator))