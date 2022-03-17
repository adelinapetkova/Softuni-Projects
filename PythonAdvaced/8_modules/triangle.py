def triangle(n):
    my_list = []
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            my_list.append(str(j))
        print(' '.join(my_list))
        my_list = []

    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            my_list.append(str(j))
        print(' '.join(my_list))
        my_list = []


