first_number = int(input())
second_number = int(input())

for first in range(first_number // 1000, second_number // 1000 + 1):
    for second in range((first_number // 100) % 10, (second_number // 100) % 10 + 1):
        for third in range((first_number // 10) % 10, (second_number // 10) % 10 + 1):
            for fourth in range(first_number % 10, second_number % 10 + 1):
                if first % 2 == 1 and second % 2 == 1 and third % 2 == 1 and fourth % 2 == 1:
                    print(f'{first}{second}{third}{fourth}', end=' ')
