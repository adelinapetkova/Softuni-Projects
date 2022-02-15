def odd_even(command, nums):
    if command == 'Odd':
        sequence_sum = sum(filter(lambda x: x % 2 == 1, nums))
    else:
        sequence_sum = sum(filter(lambda x: x % 2 == 0, nums))

    result = sequence_sum * len(nums)
    return result


word = input()
numbers = [int(el) for el in input().split()]
print(odd_even(word, numbers))
