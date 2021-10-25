import re

text = input()
regex = r'%(?P<name>[A-Z][a-z]+)%([^\|\$%\.]+)?<(?P<product>.+)>([^\|\$%\.]+)?\|(?P<quantity>\d+)\|([^\|\$%\.\d]+)?' \
        r'(?P<price>\d+(\.\d+)?)\$'

total = 0
while not text == 'end of shift':
    valid_order = re.finditer(regex, text)
    if not valid_order == None:
        for order in valid_order:
            totalPrice = int(order.group('quantity')) * float(order.group('price'))
            total += totalPrice
            print(f'{order.group("name")}: {order.group("product")} - {totalPrice:.2f}')
    text = input()

print(f'Total income: {total:.2f}')
