n = int(input())

longest_intersection=set()

for _ in range(n):
    first_pair, second_pair = input().split('-')

    first_start, first_end = [int(num) for num in first_pair.split(',')]
    second_start, second_end = [int(num) for num in second_pair.split(',')]

    first_set = set()
    second_set = set()

    for i in range(first_start, first_end + 1):
        first_set.add(i)
    for j in range(second_start, second_end + 1):
        second_set.add(j)

    intersection=first_set.intersection(second_set)
    if len(intersection)>len(longest_intersection):
        longest_intersection=intersection


longest_intersection=[str(num) for num in longest_intersection]

print(f'Longest intersection is [{", ".join(longest_intersection)}] with length {len(longest_intersection)}')

