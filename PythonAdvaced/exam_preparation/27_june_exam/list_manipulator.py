from collections import deque


def list_manipulator(my_list, action, part, *args):
    if action == 'add' and part == 'beginning':
        my_list = deque(my_list)
        args = reversed(args)
        for el in args:
            my_list.appendleft(el)
        my_list = list(my_list)
    elif action == 'add' and part == 'end':
        for el in args:
            my_list.append(el)
    elif action == 'remove' and part == 'beginning':
        my_list = deque(my_list)
        if args:
            n = args[0]
            for i in range(n):
                my_list.popleft()
        else:
            my_list.popleft()
        my_list = list(my_list)
    elif action == 'remove' and part == 'end':
        if args:
            n = args[0]
            for i in range(n):
                my_list.pop()
        else:
            my_list.pop()

    return my_list


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
