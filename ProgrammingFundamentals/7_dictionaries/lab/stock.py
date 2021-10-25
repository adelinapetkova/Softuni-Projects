products=input().split()
products1={}

for i in range(0, len(products), 2):
    products1[products[i]]=int(products[i+1])

searched_products=input().split()

for el in searched_products:
    if el in products1:
        print(f'We have {products1[el]} of {el} left')
    else:
        print(f"Sorry, we don't have {el}")