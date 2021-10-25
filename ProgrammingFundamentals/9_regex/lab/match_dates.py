import re

dates=input()
regex=r'(?P<day>\d{2})(?P<sep>[-./])(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>\d{4})'
valid_dates=re.finditer(regex, dates)
for i in valid_dates:
    print(f'Day: {i.group("day")}, Month: {i.group("month")}, Year: {i.group("year")}')

