command = input()
total_price_without_taxes = 0
taxes = 0

while not command == 'special' and not command == 'regular':
    price = float(command)
    if price < 0:
        print('Invalid price!')
        command = input()
        continue
    else:
        total_price_without_taxes += price
        taxes += (20 * price) / 100
    command = input()

total_price = total_price_without_taxes + taxes
if total_price == 0:
    print('Invalid order!')
else:
    if command == 'special':
        total_price = (total_price * 90) / 100
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price_without_taxes:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price:.2f}$')
