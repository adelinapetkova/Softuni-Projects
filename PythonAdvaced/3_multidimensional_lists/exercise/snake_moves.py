from collections import deque

n, m = [int(el) for el in input().split()]

snake = [el for el in input()]
chars_to_attach = deque()

matrix = [deque() for _ in range(n)]

for i in range(n):
    while len(chars_to_attach) < m:
        chars_to_attach += snake
    if i % 2 == 0:
        for j in range(m):
            matrix[i].append(chars_to_attach.popleft())
    else:
        for j in range(m):
            matrix[i].appendleft(chars_to_attach.popleft())

for el in matrix:
    print(''.join(el))


