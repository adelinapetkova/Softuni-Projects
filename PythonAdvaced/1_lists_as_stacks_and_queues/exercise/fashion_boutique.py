clothes=[int(c) for c in input().split()]
capacity_of_a_rack=int(input())

racks=1
rack=0

while clothes:
    num_of_clothes=clothes[-1]
    if rack+num_of_clothes<=capacity_of_a_rack:
        rack+=num_of_clothes
        clothes.pop()
    else:
        rack=0
        racks+=1

print(racks)