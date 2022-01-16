rows, columns=[int(el) for el in input().split()]

matrix=[[] for _ in range(rows)]
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
a=0

for r in range(rows):
    for c in range(columns):
        string_to_append=alphabet[r]+alphabet[c+r]+alphabet[r]
        matrix[a].append(string_to_append)
        if len(matrix[a])==columns:
            a+=1

for el in matrix:
    print(' '.join(el))
