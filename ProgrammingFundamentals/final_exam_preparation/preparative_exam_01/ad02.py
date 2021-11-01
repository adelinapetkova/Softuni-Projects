import re

regex=r'(?P<separator>[#|])(?P<name>[a-zA-Z\s]+)(\1)(?P<date>\d{2}/\d{2}/\d{2})(\1)(?P<calories>\d+)(\1)'
text=input()

valid_products=re.finditer(regex, text)

calories=0
for product in valid_products:
    calories+=int(product.group('calories'))

days=calories//2000
print(f'You have food to last you for: {days} days!')

valid_products1=re.finditer(regex,text)

for item in valid_products1:
    print(f"Item: {item.group('name')}, Best before: {item.group('date')}, Nutrition: {item.group('calories')}")