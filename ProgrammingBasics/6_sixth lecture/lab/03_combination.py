n=int(input())
combinations=0


for first_number in range(0,n+1):
    for second_number in range(0,n+1):
        for third_number in range(0,n+1):
            if first_number+second_number+third_number==n:
                combinations+=1

print(combinations)