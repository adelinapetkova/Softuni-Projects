from collections import deque


class Robot:
    def __init__(self, name, processing_time, busy_until):
        self.name = name
        self.processing_time = int(processing_time)
        self.busy_until = busy_until


def time_to_seconds(time):
    hours, minutes, seconds = time.split(':')
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    return hours * 60 * 60 + minutes * 60 + seconds


def seconds_to_time(seconds):
    seconds %= 24 * 60 * 60
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robot_list = input().split(';')
robots = []
current_time_in_seconds = time_to_seconds(input())

for r in robot_list:
    name, process_time = r.split('-')
    robots.append(Robot(name, process_time, current_time_in_seconds))

items = deque()

while True:
    item = input()
    if item == 'End':
        break
    items.append(item)

while items:
    item_to_process = items[0]
    item_collected = False
    current_time_in_seconds += 1
    for robot in robots:
        if robot.busy_until <= current_time_in_seconds:
            items.popleft()
            item_collected = True
            robot.busy_until = robot.processing_time + current_time_in_seconds
            print(f'{robot.name} - {item_to_process} [{seconds_to_time(current_time_in_seconds)}]')
            break
    if not item_collected:
        items.popleft()
        items.append(item_to_process)
