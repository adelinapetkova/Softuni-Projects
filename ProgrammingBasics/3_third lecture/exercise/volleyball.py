import math

normal_or_leap=input()
p=int(input())
home_goings=int(input())

holiday_plays=(2/3)*p
weekend_plays_at_sofia=(3/4)*(48-home_goings)
home_plays=home_goings

total_plays=home_plays+holiday_plays+weekend_plays_at_sofia

if normal_or_leap=='leap':
    total_plays=math.floor(1.15*total_plays)
    print(total_plays)
elif normal_or_leap=='normal':
    print(math.floor(total_plays))
