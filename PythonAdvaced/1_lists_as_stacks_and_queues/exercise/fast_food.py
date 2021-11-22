from collections import deque

clients = deque()
food_quantity = int(input())

orders = input().split()
orders = [int(order) for order in orders]

for order in orders:
    clients.append(order)

print(max(clients))

orders_complete = True

while clients:
    client = clients[0]
    if client <= food_quantity:
        food_quantity -= client
        clients.popleft()
    else:
        orders_complete = False
        clientss = [str(cl) for cl in clients]
        print(f'Orders left: {" ".join(clientss)}')
        break

if orders_complete:
    print('Orders complete')
