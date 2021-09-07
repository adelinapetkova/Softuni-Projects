numbers=[int(el) for el in input().split(', ')]

print('Positive:',', '.join([str(el) for el in numbers if el>=0]))
print('Negative:',', '.join([str(el) for el in numbers if el<0]))
print('Even:',', '.join([str(el) for el in numbers if el%2==0]))
print('Odd:',', '.join([str(el) for el in numbers if not el%2==0]))