n, m=[int(el) for el in input().split(' ')]

matrix = [[int(el) for el in input().split(' ')] for i in range(n)]

biggest_sum=0
biggest_sum_square=[]

for row in range(n-2):
    for column in range(m-2):
        current_square=[]
        for i in range(row, row+3):
            for j in range(column, column+3):
                current_square.append(matrix[i][j])
        current_sum=sum(current_square)
        if current_sum>=biggest_sum:
            biggest_sum=current_sum
            biggest_sum_square=[[], [], []]
            a=0
            for iteration in range(1,10):
                biggest_sum_square[a].append(current_square[iteration-1])
                if iteration%3==0:
                    a+=1

print(f'Sum = {biggest_sum}')
for el in biggest_sum_square:
    el=[str(num) for num in el]
    print(' '.join(el))
