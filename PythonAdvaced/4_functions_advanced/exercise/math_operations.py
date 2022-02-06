def math_operations(*args, **kwargs):
    args = [int(el) for el in args]
    if len(args) == 0:
        return kwargs
    for i in range(4):
        if len(args) == 0:
            break
        if i == 0:
            kwargs['a'] += args[0]
        elif i == 1:
            kwargs['s'] -= args[0]
        elif i == 2:
            if not args[0] == 0:
                kwargs['d'] /= args[0]
        elif i == 3:
            kwargs['m'] *= args[0]
        args.remove(args[0])
    return math_operations(*args, **kwargs)


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))