capacity = int(input())
command = input()

people_messages = {}

while not command == 'Statistics':
    if 'Add' in command:
        action, username, sent, received = command.split('=')
        sent = int(sent)
        received = int(received)
        if username not in people_messages:
            people_messages[username] = {}
            people_messages[username]['sent'] = sent
            people_messages[username]['received'] = received
    elif 'Message' in command:
        action, sender, receiver = command.split('=')
        if sender in people_messages and receiver in people_messages:
            people_messages[sender]['sent'] += 1
            people_messages[receiver]['received'] += 1
        if people_messages[sender]['sent'] + people_messages[sender]['received'] >= capacity:
            people_messages.pop(sender)
            print(f'{sender} reached the capacity!')
        if people_messages[receiver]['sent'] + people_messages[receiver]['received'] >= capacity:
            people_messages.pop(receiver)
            print(f'{receiver} reached the capacity!')
    elif 'Empty' in command:
        action, username = command.split('=')
        if username == 'All':
            people_messages = {}
        else:
            if username in people_messages:
                people_messages.pop(username)
    command = input()

print(f'Users count: {len(people_messages)}')

sorted_dict = dict(sorted(people_messages.items(), key=lambda x: (-x[1]['received'], x[0])))

for na in sorted_dict:
    print(f'{na} - {people_messages[na]["sent"] + people_messages[na]["received"]}')
