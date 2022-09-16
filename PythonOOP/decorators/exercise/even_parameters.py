import functools


def even_parameters(func):
    @functools.wraps(func)
    def wrapper(*args):
        even_arguments = True
        for element in args:
            if not isinstance(element, int):
                even_arguments = False
            elif element % 2 == 1:
                even_arguments = False

        if even_arguments:
            result = func(*args)
            return result
        return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
