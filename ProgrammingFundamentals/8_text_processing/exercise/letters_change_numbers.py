sequence = input().split()
total_sum = 0
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for el in sequence:
    number = ''
    first_letter = el[0]
    second_letter = el[len(el)-1]
    for i in range(1, len(el)-1):
        number += el[i]
    if first_letter.isupper():
        resulted_number = int(number)/(alphabet.index(first_letter.lower()) + 1)
    else:
        resulted_number = int(number)*(alphabet.index(first_letter.lower()) + 1)
    if second_letter.isupper():
        resulted_number -= (alphabet.index(second_letter.lower()) + 1)
    else:
        resulted_number += (alphabet.index(second_letter.lower()) + 1)
    total_sum += resulted_number

print(f'{total_sum:.2f}')
