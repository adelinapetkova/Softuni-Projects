from collections import deque

price_of_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = [int(el) for el in input().split()]
locks = deque([int(lock) for lock in input().split()])
intelligence = int(input())

used_bullets = 0

while bullets and locks:
    used_bullets += 1
    bullet = bullets.pop()
    lock = locks.popleft()
    if lock >= bullet:
        print('Bang!')
    else:
        locks.appendleft(lock)
        print('Ping!')
    if used_bullets % size_of_gun_barrel == 0 and bullets:
        print('Reloading!')

money_for_bullets = used_bullets * price_of_bullet
money_earned = intelligence - money_for_bullets

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f'{len(bullets)} bullets left. Earned ${money_earned}')
