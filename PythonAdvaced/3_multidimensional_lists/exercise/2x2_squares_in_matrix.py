n, m=[int(el) for el in input().split(' ')]

matrix = [[el for el in input().split(' ')] for i in range(n)]

identical_squares=0

for i in range(n-1):
    for j in range(m-1):
        characters_set=set()
        characters_set.add(matrix[i][j])
        characters_set.add(matrix[i][j+1])
        characters_set.add(matrix[i+1][j])
        characters_set.add(matrix[i+1][j+1])
        if len(characters_set)==1:
            identical_squares+=1

print(identical_squares)
