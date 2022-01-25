rows=int(input())

matrix=[[int(el) for el in input().split(', ')] for i in range(rows)]

flat_matrix=[]

for el in matrix:
    flat_matrix+=el
print(flat_matrix)