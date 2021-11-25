from collections import deque

n = int(input())
liters_in_tank = 0
pumps=deque()
copy_pumps=deque()

for _ in range(n):
    pump = [int(c) for c in input().split()]
    pumps.append(pump)
    copy_pumps.append(pump)

found_starting_point=False

while not found_starting_point:
    for pump in pumps:
        liters, km_to_next_pump=pump
        liters_in_tank+=liters
        liters_in_tank-=km_to_next_pump
        if liters_in_tank<0:
            liters_in_tank=0
            first_pump=pumps.popleft()
            pumps.append(first_pump)
            break
        if pumps.index(pump)==len(pumps)-1:
            found_starting_point=True

starting_pump=pumps[0]

print(copy_pumps.index(starting_pump))
