import math

name_of_series=input()
episode_minutes=int(input())
break_minutes=int(input())

lunch_minutes=break_minutes/8
relax_minutes=break_minutes/4

break_minutes=break_minutes-(lunch_minutes+relax_minutes)

if break_minutes>=episode_minutes:
    print(f'You have enough time to watch {name_of_series} and left with {math.ceil(break_minutes-episode_minutes)} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_of_series}, you need {math.ceil(episode_minutes-break_minutes)} more minutes.")