def get_magic_triangle(n):
    magic_triangle=[[1], [1,1]]
    for i in range(3,n+1):
        current_row=[]
        for j in range(i):
            if j>=len(magic_triangle[i-2]):
                element=magic_triangle[i-2][j-1]
            elif 0<=j-1<i-1:
                element=magic_triangle[i-2][j]+magic_triangle[i-2][j-1]
            else:
                element=magic_triangle[i-2][j]

            current_row.append(element)

        magic_triangle.append(current_row)

    return magic_triangle


triangle=get_magic_triangle(34)

for el in triangle:
    print(el)