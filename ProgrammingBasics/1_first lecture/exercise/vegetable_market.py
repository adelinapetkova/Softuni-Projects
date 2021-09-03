vegetables_price=float(input())
fruits_price=float(input())
vegetable_amount=int(input())
fruit_amount=int(input())

money_for_vegetables=vegetables_price*vegetable_amount
money_for_fruits=fruits_price*fruit_amount

total_in_lv=money_for_fruits+money_for_vegetables

total_in_euro=total_in_lv/1.94

print('%1.2f' %total_in_euro)