#numbers = [int(num) for num in input().split(', ')]
#print([numbers.index(number) for number in numbers if number % 2 == 0])

numbers=list(map(lambda x: int(x),input().split(', ')))
even_indices=[]
for i in range(len(numbers)):
    if numbers[i]%2==0:
        even_indices.append(i)
print(even_indices)
