number_of_orders=int(input())
total=0

for i in range(number_of_orders):
    price_per_capsule=float(input())
    days_in_month=int(input())
    capsules_count=int(input())
    price_per_order=((days_in_month*capsules_count)*price_per_capsule)
    total+=price_per_order
    print(f'The price for the coffee is: ${price_per_order:.2f}')

print(f'Total: ${total:.2f}')