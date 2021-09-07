import sys

list1 = input().split(' ')

for i in range(0, len(list1)):
    list1[i] = int(list1[i])

command = input().split()

while command[0] != 'end':
    if command[0] == 'exchange':
        if int(command[1]) < 0 or int(command[1]) > len(list1) - 1:
            print('Invalid index')
            command = input().split()
            continue
        new_list = []
        for i in range(int(command[1]) + 1, len(list1)):
            new_list.append(int(list1[i]))
        for j in range(0, int(command[1]) + 1):
            new_list.append(int(list1[j]))
        list1 = new_list
    if command[0] == 'max':
        if command[1] == 'even':
            max_even = -sys.maxsize
            for i1 in range(len(list1)):
                if int(list1[i1]) % 2 == 0 and int(list1[i1]) >= max_even:
                    max_even = int(list1[i1])
                    index = i1
            if max_even == -sys.maxsize:
                print('No matches')
            else:
                print(index)
        elif command[1] == 'odd':
            max_odd = -sys.maxsize
            for j1 in range(len(list1)):
                if int(list1[j1]) % 2 == 1 and int(list1[j1]) >= max_odd:
                    max_odd = int(list1[j1])
                    index = j1
            if max_odd == -sys.maxsize:
                print('No matches')
            else:
                print(index)
    elif command[0] == 'min':
        if command[1] == 'even':
            min_even = sys.maxsize
            for i in range(len(list1)):
                if int(list1[i]) % 2 == 0 and int(list1[i]) <= min_even:
                    min_even = int(list1[i])
                    index = i
            if min_even == sys.maxsize:
                print('No matches')
            else:
                print(index)
        elif command[1] == 'odd':
            min_odd = sys.maxsize
            for j in range(len(list1)):
                if int(list1[j]) % 2 == 1 and int(list1[j]) <= min_odd:
                    min_odd = int(list1[j])
                    index = j
            if min_odd == sys.maxsize:
                print('No matches')
            else:
                print(index)
    if command[0] == 'first':
        if int(command[1]) > len(list1):
            print('Invalid count')
            command = input().split()
            continue
        if command[2] == 'even':
            first_n_even = []
            n = int(command[1])
            m = 0
            for number in list1:
                if int(number) % 2 == 0:
                    m += 1
                    first_n_even.append(number)
                if m == n:
                    print(first_n_even)
                    break
            if m < n:
                print(first_n_even)
            if len(first_n_even) == 0:
                print('[]')
        elif command[2] == 'odd':
            first_p_odd = []
            p = int(command[1])
            q = 0
            for number_1 in list1:
                if int(number_1) % 2 == 1:
                    q += 1
                    first_p_odd.append(number_1)
                if q == p:
                    print(first_p_odd)
                    break
            if q < p:
                print(first_p_odd)
            if len(first_p_odd) == 0:
                print('[]')
    elif command[0] == 'last':
        if int(command[1]) > len(list1):
            print('Invalid count')
            command = input().split()
            continue
        if command[2] == 'even':
            last_n1_even = []
            n1 = int(command[1])
            m1 = 0
            for i1 in range(len(list1) - 1, -1, -1):
                if int(list1[i1]) % 2 == 0:
                    m1 += 1
                    last_n1_even.append(list1[i1])
                if m1 == n1:
                    last_n1_even = last_n1_even[::-1]
                    print(last_n1_even)
                    break
            if m1 < n1:
                last_n1_even = last_n1_even[::-1]
                print(last_n1_even)
        elif command[2] == 'odd':
            last_n1_odd = []
            p1 = int(command[1])
            q1 = 0
            for i2 in range(len(list1) - 1, -1, -1):
                if int(list1[i2]) % 2 == 1:
                    q1 += 1
                    last_n1_odd.append(list1[i2])
                if q1 == p1:
                    last_n1_odd = last_n1_odd[::-1]
                    print(last_n1_odd)
                    break
            if q1 < p1:
                last_n1_odd = last_n1_odd[::-1]
                print(last_n1_odd)

    command = input().split()

print(list1)
