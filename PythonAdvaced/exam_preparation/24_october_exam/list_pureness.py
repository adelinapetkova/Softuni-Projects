from collections import deque


def best_list_pureness(my_list, k):
    my_list = deque(my_list)
    rotations = {}
    num_of_rotation = 0
    for i in range(len(my_list)):  # k+1
        pureness = 0
        for i in range(len(my_list)):
            pureness += (i * my_list[i])
        rotations[num_of_rotation] = pureness
        last_element = my_list.pop()
        my_list.appendleft(last_element)
        num_of_rotation += 1

    first_key = ''
    first_value = ''
    rotations = dict(sorted(rotations.items(), key=lambda x: (-x[1], x[0])))
    for key, value in rotations.items():
        first_key = key
        first_value = value
        break
    return f'Best pureness {first_value} after {first_key} rotations'


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
