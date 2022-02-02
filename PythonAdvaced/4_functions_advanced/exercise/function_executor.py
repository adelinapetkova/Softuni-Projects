def func_executor(*args):
    args=list(args)
    results=[]
    for el in args:
        results.append(el[0](*el[1]))
    return results


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))