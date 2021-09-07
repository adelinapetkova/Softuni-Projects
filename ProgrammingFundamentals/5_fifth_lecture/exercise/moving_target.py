targets = [int(el) for el in input().split()]
command = input().split()


def shoot(index, power):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)


def add(index, value):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print('Invalid placement!')


def strike(index, radius, removed=0):
    if 0 <= index < len(targets) and 0 <= index - radius < len(targets) and 0 <= index + radius < len(targets):
        needed_removings = len([el for el in targets if index-radius<=targets.index(el)<=index+radius])
        for el in list(targets):
            if index-radius <= targets.index(el) <= index+radius:
                targets.remove(el)
                removed += 1
            if removed == needed_removings:
                break
    else:
        print('Strike missed!')


while not command[0] == 'End':
    if command[0] == 'Shoot':
        shoot(int(command[1]), int(command[2]))
    elif command[0] == 'Add':
        add(int(command[1]), int(command[2]))
    elif command[0] == 'Strike':
        strike(int(command[1]), int(command[2]))
    command=input().split()

print('|'.join([str(el) for el in targets]))
