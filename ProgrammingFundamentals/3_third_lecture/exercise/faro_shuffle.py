elements=input().split()
count_of_shuffles=int(input())
shuffled_list=0

for _ in range(count_of_shuffles):
    first_half=[]
    second_half=[]
    for i in range(len(elements)):
        if i<len(elements)/2:
            first_half.append(elements[i])
        else:
            second_half.append(elements[i])
    shuffled_list=[]
    for j in range(len(first_half)):
        shuffled_list.append(first_half[j])
        shuffled_list.append(second_half[j])
    elements=shuffled_list

print(shuffled_list)