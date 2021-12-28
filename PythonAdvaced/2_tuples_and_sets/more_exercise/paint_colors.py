colors_list = input().split()

main_colors = ['red', 'yellow', 'blue']
secondary_colors = ['orange', 'purple', 'green']

found_colors = []

while len(colors_list) > 1:
    first_substring = colors_list[0]
    second_substring = colors_list[-1]
    result = first_substring + second_substring
    result1 = second_substring + first_substring
    if result in main_colors or result in secondary_colors:
        found_colors.append(result)
        colors_list.remove(first_substring)
        colors_list.remove(second_substring)
    elif result1 in main_colors or result1 in secondary_colors:
        found_colors.append(result1)
        colors_list.remove(first_substring)
        colors_list.remove(second_substring)
    else:
        first_substring_to_return = ''
        second_substring_to_return = ''
        for i in range(0, len(first_substring) - 1):
            first_substring_to_return += first_substring[i]
        for j in range(0, len(second_substring) - 1):
            second_substring_to_return += second_substring[j]
        colors_list.remove(first_substring)
        colors_list.remove(second_substring)
        if len(colors_list) % 2 == 0:
            index_to_insert = len(colors_list) / 2
            if not first_substring_to_return == '':
                colors_list.insert(int(index_to_insert), first_substring_to_return)
            if len(colors_list) % 2 == 1:
                if not second_substring_to_return == '':
                    colors_list.insert(int(index_to_insert + 1), second_substring_to_return)
            else:
                if not second_substring_to_return == '':
                    colors_list.insert(int(index_to_insert), second_substring_to_return)
        else:
            index_to_insert = len(colors_list) // 2
            if not first_substring_to_return == '':
                colors_list.insert(int(index_to_insert), first_substring_to_return)
            if len(colors_list) % 2 == 0:
                if not second_substring_to_return == '':
                    colors_list.insert(int(index_to_insert + 1), second_substring_to_return)
            else:
                if not second_substring_to_return == '':
                    colors_list.insert(int(index_to_insert), second_substring_to_return)

if len(colors_list) == 1:
    if colors_list[0] in main_colors or colors_list[0] in secondary_colors:
        found_colors.append(colors_list[0])
        colors_list.remove(colors_list[0])

for color in found_colors:
    if color in secondary_colors:
        if color == 'orange' and not ('red' in found_colors and 'yellow' in found_colors):
            found_colors.remove(color)
        elif color == 'purple' and not ('red' in found_colors and 'blue' in found_colors):
            found_colors.remove(color)
        elif color == 'green' and not ('blue' in found_colors and 'yellow' in found_colors):
            found_colors.remove(color)

print(found_colors)
