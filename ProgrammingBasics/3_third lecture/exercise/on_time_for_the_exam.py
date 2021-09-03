exam_hour=int(input())
exam_minutes=int(input())
arriving_hour=int(input())
arriving_minutes=int(input())

exam_time=exam_hour*60 + exam_minutes
arriving_time=arriving_hour*60 + arriving_minutes

if arriving_time<(exam_time-30):
    print('Early')
    early_minutes=exam_time-arriving_time
    hours=early_minutes//60
    minutes=early_minutes%60
    if hours==0:
        print(f'{minutes} minutes before the start')
    elif hours>0:
        if minutes<10:
            print(f'{hours}:0{minutes} hours before the start')
        else:
            print(f'{hours}:{minutes} hours before the start')
elif (exam_time-30)<=arriving_time<=exam_time:
    print('On time')
    on_time_minutes=exam_time-arriving_time
    if on_time_minutes==0:
        print('On time')
    else:
        print(f'{on_time_minutes} minutes before the start')
elif arriving_time>exam_time:
    print('Late')
    late_minutes=arriving_time-exam_time
    hours=late_minutes//60
    minutes=late_minutes%60
    if hours==0:
        print(f'{minutes} minutes after the start')
    elif hours>0:
        if minutes<10:
            print(f'{hours}:0{minutes} hours after the start')
        else:
            print(f'{hours}:{minutes} hours after the start')