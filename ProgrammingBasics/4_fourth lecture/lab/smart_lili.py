age=int(input())
washing_machine_price=float(input())
toy_price=int(input())

present_toys=0
present_money=0
total_money=0

for i in range(1,age+1):
    if i%2==1:
        present_toys+=1
    else:
        present_money+=10
        total_money+=present_money

brother_taking_money=age//2*1.00

total_money=total_money-brother_taking_money
money_from_toys=present_toys*toy_price

final_budget=total_money+money_from_toys

if final_budget>=washing_machine_price:
    left=final_budget-washing_machine_price
    print(f'Yes! {left:.2f}')
else:
    needed=washing_machine_price-final_budget
    print(f'No! {needed:.2f}')