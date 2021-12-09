from collections import deque

chocolate = [int(num) for num in input().split(', ')]
milk = deque([int(num) for num in input().split(', ')])

milkshakes = 0
enough_milkshakes = True

while milkshakes < 5:
    if len(chocolate) == 0 or len(milk) == 0:
        enough_milkshakes = False
        break

    chocolate_value = chocolate[-1]
    milk_value = milk[0]
    if chocolate_value <= 0 or milk_value <= 0:
        if chocolate_value <= 0:
            chocolate.pop()
        if milk_value <= 0:
            milk.popleft()
        continue

    if chocolate_value == milk_value:
        milkshakes += 1
        chocolate.pop()
        milk.popleft()
    else:
        milk.popleft()
        milk.append(milk_value)
        chocolate.pop()
        chocolate.append(chocolate_value - 5)

if enough_milkshakes:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolate:
    chocolate = [str(ch) for ch in chocolate]
    print(f'Chocolate: {", ".join(chocolate)}')
else:
    print('Chocolate: empty')

if milk:
    milk = [str(m) for m in milk]
    print(f'Milk: {", ".join(milk)}')
else:
    print('Milk: empty')
