numbers = [int(el) for el in input().split(', ')]
group = 10

while len(numbers) > 0:
    list_of_numbers = []
    for num in list(numbers):
        if num <= group:
            list_of_numbers.append(num)
            numbers.remove(num)
    print(f"Group of {group}'s: {list_of_numbers}")
    group += 10
