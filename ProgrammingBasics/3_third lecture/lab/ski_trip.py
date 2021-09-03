days=int(input())
room_type=input()
rate=input()

nights=days-1
discount=0
price_of_room_per_night=0

if room_type=='room for one person':
    price_of_room_per_night=18
    discount=0
elif room_type=='apartment':
    price_of_room_per_night=25
    if days<10:
        discount=0.3
    elif 10<=days<=15:
        discount=0.35
    elif days>15:
        discount=0.5
elif room_type=='president apartment':
    price_of_room_per_night=35
    if days<10:
        discount=0.1
    elif 10<=days<=15:
        discount=0.15
    elif days>15:
        discount=0.2

total=(price_of_room_per_night-(price_of_room_per_night*discount))*nights

if rate=='positive':
    final_price=total+(0.25*total)
    print(f'{final_price:.2f}')
elif rate=='negative':
    final_price=total-(0.1*total)
    print(f'{final_price:.2f}')