resource = input()
resources = {}

while not resource == 'stop':
    quantity = int(input())
    if resource not in resources:
        resources[resource] = quantity
    else:
        resources[resource] += quantity
    resource = input()

for key, value in resources.items():
    print(f'{key} -> {value}')
