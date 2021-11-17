from collections import deque

names=input().split()
players=deque()

for name in names:
    players.append(name)

n=int(input())

while len(players)>1:
    for i in range(1, n + 1):
        if not i == n:
            moving = players.popleft()
            players.append(moving)
        else:
            removed = players.popleft()
            print(f'Removed {removed}')

print(f'Last is {players[0]}')