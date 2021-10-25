countries=input().split(', ')
capitals=input().split(', ')

a=dict(zip(countries,capitals))

for key, value in a.items():
    print(f'{key} -> {value}')