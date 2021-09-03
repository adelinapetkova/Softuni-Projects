days_off=int(input())

working_day_minutes=63
day_off_minutes=127

working_days=365-days_off

minutes_per_year=(days_off*day_off_minutes)+(working_day_minutes*working_days)

if minutes_per_year>30000:
    print('Tom will run away')
    excess_minutes=minutes_per_year-30000
    hours=excess_minutes//60
    minutes=excess_minutes%60
    print(f'{hours} hours and {minutes} minutes more for play')
elif minutes_per_year<30000:
    print('Tom sleeps well')
    needed_minutes=30000-minutes_per_year
    hours=needed_minutes//60
    minutes=needed_minutes%60
    print(f'{hours} hours and {minutes} minutes less for play')