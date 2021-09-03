import math

needed_hours=int(input())
days=int(input())
workers=int(input())

working_days=days*0.9
working_hours=working_days*8
extra_hours=(workers*2)*days
total_hours=working_hours+extra_hours

if total_hours>=needed_hours:
    left_hours=math.floor(total_hours-needed_hours)
    print(f'Yes!{left_hours} hours left.')
elif total_hours<needed_hours:
    more_hours=math.ceil(needed_hours-total_hours)
    print(f'Not enough time!{more_hours} hours needed.')
