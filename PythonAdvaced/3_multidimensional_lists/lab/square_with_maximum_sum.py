n, m=[int(el) for el in input().split(', ')]

matrix = [[int(el) for el in input().split(', ')] for i in range(n)]

biggest_sum=0
biggest_sum_matrix=[[], []]

for i in range(n-1):
    for j in range(m-1):
        elements_sum=0
        elements_sum+=matrix[i][j]
        elements_sum+=matrix[i][j+1]
        elements_sum+=matrix[i+1][j]
        elements_sum+=matrix[i+1][j+1]
        if elements_sum>biggest_sum:
            biggest_sum=elements_sum
            biggest_sum_matrix=[[], []]
            biggest_sum_matrix[0].append(matrix[i][j])
            biggest_sum_matrix[0].append(matrix[i][j+1])
            biggest_sum_matrix[1].append(matrix[i+1][j])
            biggest_sum_matrix[1].append(matrix[i+1][j+1])

for el in biggest_sum_matrix:
    el=[str(a) for a in el]
    print(' '.join(el))

print(biggest_sum)