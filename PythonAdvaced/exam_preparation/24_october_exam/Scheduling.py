jobs=[el for el in input().split(', ')]
index_to_break=int(input())
total_cycles=0

while jobs:
    numbers=[]
    for el in jobs:
        if el.isdigit():
            numbers.append(int(el))
    min_number=min(numbers)
    index_of_min_num=jobs.index(str(min_number))
    if index_of_min_num==index_to_break:
        total_cycles+=min_number
        break
    total_cycles+=min_number
    jobs[index_of_min_num]=''

print(total_cycles)
