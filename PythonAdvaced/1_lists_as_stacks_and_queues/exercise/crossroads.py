from collections import deque

green_light = int(input())
free_window = int(input())

green_light_seconds = green_light
free_window_seconds = free_window

cars = deque()
total_cars_passed = 0
crash = False

while True:
    command = input()
    if command == 'END':
        break
    if command == 'green':
        green_light_seconds = green_light
        free_window_seconds = free_window
        while cars:
            car = cars[0]
            if len(car) <= green_light_seconds:
                green_light_seconds -= len(car)
                cars.popleft()
                total_cars_passed += 1
            elif green_light_seconds == 0:
                break
            else:
                for i in range(len(car)):
                    green_light_seconds -= 1
                    if green_light_seconds == 0:
                        chars_to_exit = len(car) - i - 1
                        if chars_to_exit <= free_window_seconds:
                            cars.popleft()
                            total_cars_passed += 1
                            break
                        else:
                            num_of_chars_unable_to_exit = chars_to_exit - free_window_seconds
                            crashed_char = car[len(car) - num_of_chars_unable_to_exit]
                            crash = True
                            print('A crash happened!')
                            print(f'{car} was hit at {crashed_char}.')
                            break
            if crash:
                break
    else:
        cars.append(command)
    if crash:
        break

if not crash:
    print('Everyone is safe.')
    print(f'{total_cars_passed} total cars passed the crossroads.')