def valid_indices_check(r1, c1, r2, c2, rows, columns):
    if 0 <= r1 < rows and 0 <= r2 < rows and 0 <= c1 < columns and 0 <= c2 < columns:
        return True
    else:
        return False


n, m = [int(el) for el in input().split()]

matrix = [[el for el in input().split()] for i in range(n)]

command = input()

while not command == 'END':
    split_command = command.split()
    if not len(split_command) == 5:
        print('Invalid input!')
        command = input()
        continue
    else:
        action, r1, c1, r2, c2 = split_command
        r1 = int(r1)
        r2 = int(r2)
        c1 = int(c1)
        c2 = int(c2)
        if action == 'swap' and valid_indices_check(r1, c1, r2, c2, n, m):
            matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
            for el in matrix:
                el = [str(ch) for ch in el]
                print(' '.join(el))
        else:
            command = input()
            print('Invalid input!')
            continue
    command = input()
