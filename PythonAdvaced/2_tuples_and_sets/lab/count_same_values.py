numbers=[float(num) for num in input().split()]

numbers_dictionary={}

for num in numbers:
    if num not in numbers_dictionary:
        numbers_dictionary[num]=0
    numbers_dictionary[num]+=1

for num, times in numbers_dictionary.items():
    print(f'{num} - {times} times')
