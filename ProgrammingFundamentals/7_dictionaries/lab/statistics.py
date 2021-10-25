command = input()
products = {}
sum_of_quantities = 0

while not command == 'statistics':
    product, quantity = command.split(': ')
    sum_of_quantities += int(quantity)
    if product not in products:
        products[product] = int(quantity)
    else:
        products[product] += int(quantity)
    command = input()

print('Products in stock:')
for prod, quan in products.items():
    print(f'- {prod}: {quan}')

print(f'Total Products: {len(products)}')
print(f'Total Quantity: {sum_of_quantities}')
