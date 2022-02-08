def operate(sign, *args):
    if sign == '+':
        return sum(args)
    elif sign == '*':
        result = 1
        for el in args:
            result *= el
        return result
    elif sign == '-':
        result = args[0]
        for i in range(1, len(args)):
            result -= args[i]
        return result
    elif sign == '/':
        result = args[0]
        for i in range(1, len(args)):
            result /= args[i]
        return result


print(operate('+', 1, 2, 3))
print(operate('*', 3, 4))
print(operate('-', 3, 4, 5, 6))
print(operate('/', 50, 5, 2, 5))