def numbers_searching(*args):
    missing_number=0
    duplicates = set()
    smallest_value = min(args)
    biggest_value = max(args)
    for i in range(smallest_value, biggest_value + 1):
        if i not in args:
            missing_number = i
            break

    for el in args:
        n=args.count(el)
        if n>1:
            duplicates.add(el)

    duplicate_numbers=sorted(list(duplicates))
    return [missing_number,duplicate_numbers]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))