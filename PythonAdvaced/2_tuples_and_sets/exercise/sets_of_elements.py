n, m=input().split()
n=int(n)
m=int(m)

first_set=set()
second_set=set()

for i in range(n):
    num=int(input())
    first_set.add(num)

for j in range(m):
    num=int(input())
    second_set.add(num)

intersection=first_set.intersection(second_set)

for num in intersection:
    print(num)