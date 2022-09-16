import functools


def type_check(type):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(element):
            if isinstance(element, type):
                return func(element)
            else:
                return "Bad Type"

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))