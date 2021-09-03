hours=int(input())
minutes=int(input())

time_in_minutes=hours*60+minutes+15

new_hours=time_in_minutes//60
new_minutes=time_in_minutes%60

if new_hours>=24:
    new_hours=new_hours%24

if new_minutes<10:
    print(f'{new_hours}:0{new_minutes}')
else:
    print(f'{new_hours}:{new_minutes}')