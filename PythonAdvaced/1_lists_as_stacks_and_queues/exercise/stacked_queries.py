n=int(input())
stack=[]

for _ in range(n):
    command=input().split()
    action=int(command[0])
    if action==1:
        number=int(command[1])
        stack.append(number)
    elif action==2:
        if stack:
            stack.pop()
    elif action==3:
        if stack:
            print(max(stack))
    elif action==4:
        if stack:
            print(min(stack))

stack=[str(num) for num in stack]
result=[]

while stack:
    result.append(stack.pop())

print(', '.join(result))

