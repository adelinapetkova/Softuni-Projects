import re

product = input()
products = ''
while not product == 'Purchase':
    products += product
    products += ' '
    product = input()

regex = r'>>(?P<product>[a-zA-Z]+)<<(?P<price>\d+\.?\d+)!(?P<quantity>\d+)'
valid_products = re.finditer(regex, products)

total = 0

print('Bought furniture:')
for pro in valid_products:
    print(pro.group('product'))
    total += float(pro.group('price')) * int(pro.group('quantity'))

print(f'Total money spend: {total:.2f}')
