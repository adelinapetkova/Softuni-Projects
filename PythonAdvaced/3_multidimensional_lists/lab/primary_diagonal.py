rows = int(input())

matrix = [[int(el) for el in input().split(' ')] for i in range(rows)]

print(sum([matrix[i][i] for i in range(rows)]))
