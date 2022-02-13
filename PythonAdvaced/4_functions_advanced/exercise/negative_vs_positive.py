def divider(args):
    args = [int(el) for el in args]
    positive = filter(lambda x: x > 0, args)
    negative = filter(lambda x: x < 0, args)
    positive_sum = sum(positive)
    negative_sum = sum(negative)
    print(negative_sum)
    print(positive_sum)
    if abs(negative_sum) > positive_sum:
        print('The negatives are stronger than the positives')
    else:
        print('The positives are stronger than the negatives')


numbers = map(int, input().split())
divider(numbers)
