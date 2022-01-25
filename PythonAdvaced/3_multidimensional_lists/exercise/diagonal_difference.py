rows=int(input())

matrix=[[int(el) for el in input().split(' ')] for i in range(rows)]

primary_diagonal=[matrix[i][i] for i in range(rows)]
secondary_diagonal=[]

for row in range(rows):
    column=rows-row-1
    secondary_diagonal.append(matrix[row][column])

primary_diagonal_sum=sum(primary_diagonal)
secondary_diagonal_sum=sum(secondary_diagonal)

difference=abs(primary_diagonal_sum-secondary_diagonal_sum)

print(difference)