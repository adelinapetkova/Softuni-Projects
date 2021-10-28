numbers = [int(el) for el in input().split()]
average = sum(numbers) / len(numbers)

greater_than_average = []

for num in numbers:
    if num > average:
        greater_than_average.append(num)

greater_than_average.sort(reverse=True)
greater_than_average_str = [str(el) for el in greater_than_average]

if 0 < len(greater_than_average) <= 5:
    print(' '.join(greater_than_average_str))
elif len(greater_than_average)==0:
    print('No')
else:
    for i in range(5):
        print(greater_than_average_str[i], end=' ')
