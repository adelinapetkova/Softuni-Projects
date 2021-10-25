command = input()
dictionary = {}

while ':' in command:
    name, student_id, course = command.split(':')
    if course not in dictionary:
        dictionary[course] = {}
    dictionary[course][name] = student_id
    command = input()

splitted_course = ' '.join(command.split('_'))

for key, value in dictionary[splitted_course].items():
    print(f'{key} - {value}')
