matrix = [[el for el in input().split()] for _ in range(5)]

num_of_commands = int(input())

my_row = 0
my_col = 0
num_of_targets = 0
for r in range(5):
    for c in range(5):
        if matrix[r][c] == 'A':
            my_col = c
            my_row = r
        elif matrix[r][c] == 'x':
            num_of_targets += 1

shot_targets = []
for _ in range(num_of_commands):
    command = input().split()
    if command[0] == 'shoot':
        direction = command[1]
        if direction == 'right':
            row = my_row
            for col in range(my_col + 1, 5):
                if matrix[row][col] == 'x':
                    matrix[row][col] = '.'
                    num_of_targets -= 1
                    shot_targets.append([row, col])
                    break
        elif direction == 'left':
            row = my_row
            for col in range(my_col - 1, -1, -1):
                if matrix[row][col] == 'x':
                    matrix[row][col] = '.'
                    num_of_targets -= 1
                    shot_targets.append([row, col])
                    break
        elif direction == 'up':
            col = my_col
            for row in range(my_row - 1, -1, -1):
                if matrix[row][col] == 'x':
                    matrix[row][col] = '.'
                    num_of_targets -= 1
                    shot_targets.append([row, col])
                    break
        elif direction == 'down':
            col = my_col
            for row in range(my_row + 1, 5):
                if matrix[row][col] == 'x':
                    matrix[row][col] = '.'
                    num_of_targets -= 1
                    shot_targets.append([row, col])
                    break
    elif command[0] == 'move':
        direction = command[1]
        steps = int(command[2])
        if direction == 'right':
            row = my_row
            for col in range(my_col + 1, my_col + steps + 1):
                if not 0 < my_col + steps < 5:
                    break
                if matrix[row][col] == 'x':
                    break
                matrix[row][col - 1] = '.'
                matrix[row][col] = 'A'
                my_col += steps
        elif direction == 'left':
            row = my_row
            for col in range(my_col - 1, my_col - steps - 1, -1):
                if not 0 <= my_col - steps < 5:
                    break
                if matrix[row][col] == 'x':
                    break
                matrix[row][col + 1] = '.'
                matrix[row][col] = 'A'
                my_col -= steps
        elif direction == 'up':
            col = my_col
            for row in range(my_row - 1, my_row - steps - 1, -1):
                if not 0 <= my_row - steps < 5:
                    break
                if matrix[row][col] == 'x':
                    break
                matrix[row - 1][col] = '.'
                matrix[row][col] = 'A'
                my_row -= steps
        elif direction == 'down':
            col = my_col
            for row in range(my_row + 1, my_row + steps + 1):
                if not 0 < my_row + steps < 5:
                    break
                if matrix[row][col] == 'x':
                    break
                matrix[row + 1][col] = '.'
                matrix[row][col] = 'A'
                my_row += steps

    if num_of_targets == 0:
        break

if num_of_targets == 0:
    print(f'Training completed! All {len(shot_targets)} targets hit.')
    for el in shot_targets:
        print(el)
else:
    print(f'Training not completed! {num_of_targets} targets left.')
    for el in shot_targets:
        print(el)
