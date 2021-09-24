import math

people=int(input())
entry_price=float(input())
sunbed_price=float(input())
umbrella_price=float(input())

sunbeds=math.ceil(0.75*people)
umbrellas=math.ceil(people/2)

money_for_entry_fees=people*entry_price
money_for_sunbeds=sunbeds*sunbed_price
money_for_umbrellas=umbrellas*umbrella_price

total=money_for_umbrellas+money_for_sunbeds+money_for_entry_fees

print(f'{total:.2f} lv.')