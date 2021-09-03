campaign_days=int(input())
number_of_cooks=int(input())
number_of_cakes=int(input())
number_of_waffles=int(input())
number_of_pancakes=int(input())

price_of_cake=45
price_of_waffle=5.80
price_of_pancakes=3.20

money_from_cakes=number_of_cakes*price_of_cake
money_from_waffles=number_of_waffles*price_of_waffle
money_from_pancakes=number_of_pancakes*price_of_pancakes

money_per_day=(money_from_pancakes + money_from_waffles + money_from_cakes)*number_of_cooks

total=money_per_day*campaign_days

money_for_charity=total-(total*1/8)

print(money_for_charity)