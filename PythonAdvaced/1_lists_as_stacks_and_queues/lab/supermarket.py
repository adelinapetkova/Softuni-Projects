from collections import deque

text=input()
customers=deque()

while not text=='End':
    if not text=='Paid':
        customers.append(text)
    else:
        while len(customers)>0:
            print(customers.popleft())
    text=input()

print(f'{len(customers)} people remaining.')