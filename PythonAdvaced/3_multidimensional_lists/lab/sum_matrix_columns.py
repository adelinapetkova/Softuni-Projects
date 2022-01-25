n, m=[int(el) for el in input().split(', ')]

matrix=[[int(el) for el in input().split(' ')] for i in range(n)]

for i in range(m):
    column_sum=0
    for el in matrix:
        column_sum+=el[i]
    print(column_sum)