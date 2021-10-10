number_of_locations=int(input())

for i in range(number_of_locations):
    gold_per_location = 0
    expected_gold_per_day=float(input())
    days_per_location=int(input())
    for j in range(days_per_location):
        gold_per_day=float(input())
        gold_per_location+=gold_per_day
    average_gold_per_day=gold_per_location/days_per_location
    if average_gold_per_day>=expected_gold_per_day:
        print(f'Good job! Average gold per day: {average_gold_per_day:.2f}.')
    else:
        needed=expected_gold_per_day-average_gold_per_day
        print(f'You need {needed:.2f} gold.')
