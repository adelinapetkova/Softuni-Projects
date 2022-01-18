rows, columns=[int(el) for el in input().split(', ')]


matrix=[]
sum_of_matrix=0

for i in range(rows):
    element=[int(el) for el in input().split(', ')]
    sum_of_element=sum(element)
    sum_of_matrix+=sum_of_element
    matrix.append(element)

print(sum_of_matrix)
print(matrix)