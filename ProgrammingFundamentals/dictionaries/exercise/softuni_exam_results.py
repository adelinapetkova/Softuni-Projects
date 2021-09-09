command = input()
results = {}
submissions = {}

while not command == 'exam finished':
    if 'banned' not in command:
        username, language, points = command.split('-')
        if language not in submissions:
            submissions[language] = 1
        else:
            submissions[language] += 1
        if language not in results:
            results[language] = {}
        username_found = False
        for key, value in results.items():
            for key1, value1 in value.items():
                if username == key1 and language == key:
                    username_found = True
        if not username_found:
            results[language][username] = int(points)
        else:
            if int(points) > results[language][username]:
                results[language][username] = int(points)
    else:
        username, status = command.split('-')
        for key, value in results.items():
            for name in value:
                if name == username:
                    results[key][name] = 0
    command = input()

a = dict(sorted(results.items(), key=lambda x: x[0]))

names_and_points = {}
for key, value in a.items():
    for key1, value1 in value.items():
        names_and_points[key1] = value1
d = dict(sorted(names_and_points.items(), key=lambda x: (-x[1], x[0])))

print('Results:')
for key, value in d.items():
    if not value == 0:
        print(f'{key} | {value}')

print('Submissions:')
b = dict(sorted(submissions.items(), key=lambda x: (-x[1], x[0])))
for key, value in b.items():
    print(f'{key} - {submissions[key]}')
