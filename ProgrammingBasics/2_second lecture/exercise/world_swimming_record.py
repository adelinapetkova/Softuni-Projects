record=float(input())
distance=float(input())
seconds_per_meter=float(input())

resistance=(distance//15)*12.5
ivan_time=seconds_per_meter*distance+resistance

if ivan_time<record:
    print(f'Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.')
else:
    needed_seconds=ivan_time-record
    print(f'No, he failed! He was {needed_seconds:.2f} seconds slower.')