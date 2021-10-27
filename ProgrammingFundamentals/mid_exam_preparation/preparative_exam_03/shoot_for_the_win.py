targets = [int(el) for el in input().split()]
command = input()

while not command == 'End':
    index = int(command)
    if 0 <= index < len(targets) and targets[index] != -1:
        for i in range(0, len(targets)):
            if not targets[i] == -1 and index != i:
                if targets[i] > targets[index]:
                    targets[i] -= targets[index]
                else:
                    targets[i] += targets[index]
        targets[index] = -1
    command = input()


shot_targets = [el for el in targets if el == -1]
targets1 = [str(el) for el in targets]

print(f'Shot targets: {len(shot_targets)} -> {" ".join(targets1)}')
