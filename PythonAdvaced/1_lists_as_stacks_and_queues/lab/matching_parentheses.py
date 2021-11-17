expression=input()

opening_indices=[]

for i in range(0,len(expression)):
    if expression[i]=='(':
        opening_indices.append(i)
    elif expression[i]==')':
        print(expression[opening_indices.pop():(i+1)])


