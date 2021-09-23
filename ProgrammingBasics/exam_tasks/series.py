import math

name=input()
seasons=int(input())
episodes_per_season=int(input())
minutes_per_episode=float(input())
episodes=seasons*episodes_per_season
adds=0.2*minutes_per_episode*episodes

total=adds+seasons*10+episodes*minutes_per_episode

print(f'Total time needed to watch the {name} series is {math.floor(total)} minutes.')


