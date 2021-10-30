clients = int(input())
wagons = [int(el) for el in input().split()]
no_space = False

for i in range(len(wagons)):
    empty_spaces_in_wagon = 4 - wagons[i]
    if empty_spaces_in_wagon == 0 and not clients == 0:
        no_space=True
        continue
    if clients == 0 and not empty_spaces_in_wagon == 0:
        break
    if clients >= 4:
        clients -= empty_spaces_in_wagon
        wagons[i] += empty_spaces_in_wagon
    else:
        if empty_spaces_in_wagon >= clients:
            wagons[i] += clients
            clients = 0
        else:
            wagons[i] += empty_spaces_in_wagon
            clients -= empty_spaces_in_wagon

empty_spots = [el for el in wagons if el < 4]
if len(empty_spots) > 0:
    print('The lift has empty spots!')

if clients > 0 or no_space:
    print(f"There isn't enough space! {clients} people in a queue!")

wagons_as_str = [str(el) for el in wagons]
print(' '.join(wagons_as_str))
