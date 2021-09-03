import math

magnolia_price=3.25
hyacinth_price=4
rose_price=3.5
cactus_price=8

magnolias=int(input())
hyacinths=int(input())
roses=int(input())
cactuses=int(input())
price_of_gift=float(input())

money_from_magnolias=magnolias*magnolia_price
money_from_hyacinths=hyacinths*hyacinth_price
money_from_roses=roses*rose_price
money_from_cactuses=cactuses*cactus_price

total=money_from_cactuses+money_from_roses+money_from_magnolias+money_from_hyacinths

final_money=0.95*total

if final_money>=price_of_gift:
    left=math.floor(final_money-price_of_gift)
    print(f'She is left with {left} leva.')
else:
    needed=math.ceil(price_of_gift-final_money)
    print(f'She will have to borrow {needed} leva.')



