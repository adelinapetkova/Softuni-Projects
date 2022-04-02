def shopping_list(budget, **kwargs):
    if budget < 100:
        return 'You do not have enough budget.'
    else:
        types_of_bought_products = []
        bought_products = []
        product_number = 1
        for product, price_quantity in kwargs.items():
            if product_number > 5:
                break
            price = price_quantity[0]
            quantity = price_quantity[1]
            if price * quantity <= budget:
                if product not in types_of_bought_products:
                    types_of_bought_products.append(product)
                    product_number += 1
                budget -= price * quantity
                bought_products.append(f'You bought {product} for {price * quantity:.2f} leva.')
            if budget <= 0:
                break

        return '\n'.join(bought_products)


print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10), ))
print(shopping_list(20, jeans=(19.99, 1), ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
