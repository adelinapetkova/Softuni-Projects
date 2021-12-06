n=int(input())

reservations=set()

for _ in range(n):
    reservation_code=input()
    reservations.add(reservation_code)

while True:
    code=input()
    if code=='END':
        break
    reservations.remove(code)

vip=[]
regular=[]

for guest in reservations:
    if guest[0].isdigit():
        vip.append(guest)
    else:
        regular.append(guest)

print(len(reservations))

vip=sorted(vip)
regular=sorted(regular)

[print(g) for g in vip]
[print(r) for r in regular]