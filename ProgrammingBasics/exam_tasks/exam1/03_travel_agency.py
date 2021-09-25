town=input()
package=input()
vip_discount=input()
days=int(input())
day_price=0

if (town=='Bansko' or town=='Borovets' or town=='Varna' or town=='Burgas') and (package=='withEquipment' or package=='noEquipment' or package=='withBreakfast' or package=='noBreakfast') and days>0:
  if town=='Bansko' or town=='Borovets':
    if package=='withEquipment':
        if vip_discount=='yes':
            day_price=0.9*100
        else:
            day_price=100
    elif package=='noEquipment':
        if vip_discount=='yes':
            day_price=0.95*80
        else:
            day_price=80
  elif town=='Varna' or town=='Burgas':
    if package=='withBreakfast':
        if vip_discount=='yes':
            day_price=0.88*130
        else:
            day_price=130
    elif package=='noBreakfast':
        if vip_discount=='yes':
            day_price=0.93*100
        else:
            day_price=100
  if days>7:
      price=day_price*(days-1)
  else:
      price=day_price*days
  print(f'The price is {price:.2f}lv! Have a nice time!')
elif days<=0:
    print(f'Days must be positive number!')
else:
    print(f'Invalid input!')


