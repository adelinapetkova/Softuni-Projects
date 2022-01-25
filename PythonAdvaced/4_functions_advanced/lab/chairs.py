def combinations(names, seats, index, comb):
    if len(comb) == seats:
        print(', '.join(comb))
        return
    for i in range(index, len(names)):
        comb.append(names[i])
        combinations(names, seats, i + 1, comb)
        comb.pop()


list_of_names=input().split(', ')
num_of_seats=int(input())
combinations(list_of_names, num_of_seats, 0, [])
