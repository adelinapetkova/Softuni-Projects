list_of_products = input().split('|')
command = input()

while not command == 'Shop!':
    splited_command = command.split('%')
    if splited_command[0] == 'Important':
        if splited_command[1] in list_of_products:
            list_of_products.remove(splited_command[1])
            list_of_products.insert(0, splited_command[1])
        else:
            list_of_products.insert(0, splited_command[1])
    elif splited_command[0] == 'Add':
        if not splited_command[1] in list_of_products:
            list_of_products.append(splited_command[1])
        else:
            print('The product is already in the list.')
    elif splited_command[0] == 'Swap':
        if splited_command[1] in list_of_products and splited_command[2] in list_of_products:
            index_first_product = list_of_products.index(splited_command[1])
            index_second_product = list_of_products.index(splited_command[2])
            list_of_products[index_first_product], list_of_products[index_second_product] = \
                list_of_products[index_second_product], list_of_products[index_first_product]
        else:
            if splited_command[1] not in list_of_products:
                print(f'Product {splited_command[1]} missing!')
            else:
                print(f'Product {splited_command[2]} missing!')
    elif splited_command[0] == 'Remove':
        if splited_command[1] in list_of_products:
            list_of_products.remove(splited_command[1])
        else:
            print(f"Product {splited_command[1]} isn't in the list.")
    elif splited_command[0] == 'Reversed':
        list_of_products.reverse()
    command = input()

for i in range(1,len(list_of_products)+1):
    print(f'{i}. {list_of_products[i-1]}')