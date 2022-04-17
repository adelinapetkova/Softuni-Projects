n = int(input())


def print_line(stars_count, spaces_count):
    list_spaces = ''.join([' '] * spaces_count)
    list_stars = ' '.join(['*'] * stars_count)
    print(list_spaces + list_stars)


for i in range(n):
    spaces = n - i - 1
    stars = i + 1
    print_line(stars, spaces)

for j in range(n - 2, -1, -1):
    spaces = n - j - 1
    stars = j + 1
    print_line(stars, spaces)

