n = int(input())

odd_values = set()
even_values = set()

for i in range(1, n + 1):
    name = input()
    name_value = 0

    for ch in name:
        name_value += ord(ch)

    name_value = name_value // i
    if name_value % 2 == 0:
        even_values.add(name_value)
    else:
        odd_values.add(name_value)

sum_odd = sum(odd_values)
sum_even = sum(even_values)

if sum_odd == sum_even:
    union = [str(num) for num in odd_values.union(even_values)]
    print(', '.join(union))
elif sum_odd > sum_even:
    difference = [str(num) for num in odd_values.difference(even_values)]
    print(', '.join(difference))
else:
    symmetric_difference = [str(num) for num in odd_values.symmetric_difference(even_values)]
    print(', '.join(symmetric_difference))
