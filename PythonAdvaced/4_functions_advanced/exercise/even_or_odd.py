def even_odd(*args):
    command=args[-1]
    args=list(args)
    args.pop()
    if command=='odd':
        nums_list=list(filter(lambda x: x%2==1, args))
    else:
        nums_list = list(filter(lambda x: x % 2 == 0, args))
    return nums_list


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'odd'))
