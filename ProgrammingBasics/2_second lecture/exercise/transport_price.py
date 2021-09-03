kilometers=int(input())
day_or_night=input()

if day_or_night == 'day':
    taxi = 0.7 + 0.79 * kilometers
elif day_or_night == 'night':
    taxi = 0.7 + 0.9 * kilometers

if kilometers>=100:
    train=kilometers*0.06
    bus=kilometers*0.09
    if train<bus and train<taxi:
        print(f'{train:.2f}')
    elif bus<train and bus<taxi:
        print(f'{bus:.2f}')
    elif taxi<bus and taxi<train:
        print(f'{taxi:.2f}')
elif 100>kilometers>=20:
    bus = kilometers * 0.09
    if bus<taxi:
        print(f'{bus:.2f}')
    elif taxi<=bus:
        print(f'{taxi:.2f}')
else:
    print(f'{taxi:.2f}')


