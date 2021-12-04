n=int(input())

el_set=set()

for _ in range(n):
    elements=input().split()
    for el in elements:
        el_set.add(el)

for e in el_set:
    print(e)


