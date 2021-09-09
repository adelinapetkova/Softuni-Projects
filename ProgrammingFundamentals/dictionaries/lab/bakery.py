products=input().split()
products1={}

for i in range(0, len(products), 2):
    products1[products[i]]=int(products[i+1])

print(products1)