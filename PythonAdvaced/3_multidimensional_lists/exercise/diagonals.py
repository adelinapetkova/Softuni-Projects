rows=int(input())

matrix=[[int(el) for el in input().split(', ')] for i in range(rows)]

primary_diagonal=[matrix[i][i] for i in range(rows)]
secondary_diagonal=[]

for row in range(rows):
    column=rows-row-1
    secondary_diagonal.append(matrix[row][column])

primary_diagonal_sum=sum(primary_diagonal)
secondary_diagonal_sum=sum(secondary_diagonal)
primary_diagonal=[str(el) for el in primary_diagonal]
secondary_diagonal=[str(el) for el in secondary_diagonal]
print(f'Primary diagonal: {", ".join(primary_diagonal)}. Sum: {primary_diagonal_sum}')
print(f'Secondary diagonal: {", ".join(secondary_diagonal)}. Sum: {secondary_diagonal_sum}')