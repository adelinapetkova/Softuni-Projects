import re

regex=r'(?P<sep>[/|=])(?P<destination>[A-Z][A-Za-z]{2,})(?P=sep)'
text=input()
valid_dest=re.finditer(regex,text)
destinations=[]

for d in valid_dest:
    destinations.append(d.group('destination'))

print(f"Destinations: {', '.join(destinations)}")

travel_points=0

for de in destinations:
    travel_points+=len(de)

print(f'Travel Points: {travel_points}')