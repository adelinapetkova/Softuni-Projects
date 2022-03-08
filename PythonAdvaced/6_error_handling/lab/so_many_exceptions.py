for _ in range(3):
    result=1
    numbers_list = [int(el) for el in input().split(', ')]
    for i in range(len(numbers_list)):
        number = numbers_list[i]
        if number <= 5:
            result *= number
        else:
            result /= number
    print(int(result))
        