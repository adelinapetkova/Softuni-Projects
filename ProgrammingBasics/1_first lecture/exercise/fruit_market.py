strawberries_price=float(input())
amount_of_bananas=float(input())
amount_of_oranges=float(input())
amount_of_raspberries=float(input())
amount_of_strawberries=float(input())

raspberries_price=1/2*strawberries_price
oranges_price= raspberries_price - (0.4*raspberries_price)
bananas_price=0.2*raspberries_price

money_for_strawberries=strawberries_price*amount_of_strawberries
money_for_raspberries=raspberries_price*amount_of_raspberries
money_for_oranges=oranges_price*amount_of_oranges
money_for_bananas=bananas_price*amount_of_bananas

total=money_for_raspberries+money_for_bananas+money_for_oranges+money_for_strawberries

print(total)

