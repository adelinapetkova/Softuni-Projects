tickets1 = input().split(',')
tickets = [el.strip() for el in tickets1]

for ticket in tickets:
    if not len(ticket) == 20:
        print('invalid ticket')
        continue
    elif '@' in ticket:
        left_half = ''
        right_half = ''
        for i in range(len(ticket)):
            if i < len(ticket) / 2:
                left_half += ticket[i]
            else:
                right_half += ticket[i]
        num_of_special_symbols_left = 0
        num_of_special_symbols_right = 0
        for i in range(len(left_half)):
            if left_half[i] == '@':
                num_of_special_symbols_left += 1
                if i + 1 < len(left_half) and not left_half[i + 1] == '@':
                    if num_of_special_symbols_left >= 6:
                        break
                    else:
                        num_of_special_symbols_left = 0
        for i in range(len(right_half)):
            if right_half[i] == '@':
                num_of_special_symbols_right += 1
                if i + 1 < len(right_half) and not right_half[i + 1] == '@':
                    if num_of_special_symbols_right >= 6:
                        break
                    else:
                        num_of_special_symbols_right = 0
        if 10 > num_of_special_symbols_right >= 6 or 10 > num_of_special_symbols_left >= 6:
            print(f'ticket "{ticket}" - {min(num_of_special_symbols_left,num_of_special_symbols_right)}@')
        elif num_of_special_symbols_left == 10 and num_of_special_symbols_right==10:
            print(f'ticket "{ticket}" - {num_of_special_symbols_right}@ Jackpot!')
        else:
            print(f'ticket "{ticket}" - no match')
    elif '#' in ticket:
        left_half = ''
        right_half = ''
        for i in range(len(ticket)):
            if i < len(ticket) / 2:
                left_half += ticket[i]
            else:
                right_half += ticket[i]
        num_of_special_symbols_left = 0
        num_of_special_symbols_right = 0
        for i in range(len(left_half)):
            if left_half[i] == '#':
                num_of_special_symbols_left += 1
                if i + 1 < len(left_half) and not left_half[i + 1] == '#':
                    if num_of_special_symbols_left >= 6:
                        break
                    else:
                        num_of_special_symbols_left = 0
        for i in range(len(right_half)):
            if right_half[i] == '#':
                num_of_special_symbols_right += 1
                if i + 1 < len(right_half) and not right_half[i + 1] == '#':
                    if num_of_special_symbols_right >= 6:
                        break
                    else:
                        num_of_special_symbols_right = 0
        if 10 > num_of_special_symbols_right >= 6 or 10 > num_of_special_symbols_left >= 6:
            print(f'ticket "{ticket}" - {min(num_of_special_symbols_left,num_of_special_symbols_right)}#')
        elif num_of_special_symbols_left == 10 and num_of_special_symbols_right == 10:
            print(f'ticket "{ticket}" - {num_of_special_symbols_right}# Jackpot!')
        else:
            print(f'ticket "{ticket}" - no match')
    elif '$' in ticket:
        left_half = ''
        right_half = ''
        for i in range(len(ticket)):
            if i < len(ticket) / 2:
                left_half += ticket[i]
            else:
                right_half += ticket[i]
        num_of_special_symbols_left = 0
        num_of_special_symbols_right = 0
        for i in range(len(left_half)):
            if left_half[i] == '$':
                num_of_special_symbols_left += 1
                if i + 1 < len(left_half) and not left_half[i + 1] == '$':
                    if num_of_special_symbols_left >= 6:
                        break
                    else:
                        num_of_special_symbols_left = 0
        for i in range(len(right_half)):
            if right_half[i] == '$':
                num_of_special_symbols_right += 1
                if i + 1 < len(right_half) and not right_half[i + 1] == '$':
                    if num_of_special_symbols_right >= 6:
                        break
                    else:
                        num_of_special_symbols_right = 0
        if 10 > num_of_special_symbols_right >= 6 or 10 > num_of_special_symbols_left >= 6:
            print(f'ticket "{ticket}" - {min(num_of_special_symbols_left,num_of_special_symbols_right)}$')
        elif num_of_special_symbols_left == 10 and num_of_special_symbols_right == 10:
            print(f'ticket "{ticket}" - {num_of_special_symbols_right}$ Jackpot!')
        else:
            print(f'ticket "{ticket}" - no match')
    elif '^' in ticket:
        left_half = ''
        right_half = ''
        for i in range(len(ticket)):
            if i < len(ticket) / 2:
                left_half += ticket[i]
            else:
                right_half += ticket[i]
        num_of_special_symbols_left = 0
        num_of_special_symbols_right = 0
        for i in range(len(left_half)):
            if left_half[i] == '^':
                num_of_special_symbols_left += 1
                if i + 1 < len(left_half) and not left_half[i + 1] == '^':
                    if num_of_special_symbols_left >= 6:
                        break
                    else:
                        num_of_special_symbols_left = 0
        for i in range(len(right_half)):
            if right_half[i] == '^':
                num_of_special_symbols_right += 1
                if i + 1 < len(right_half) and not right_half[i + 1] == '^':
                    if num_of_special_symbols_right >= 6:
                        break
                    else:
                        num_of_special_symbols_right = 0
        if 10 > num_of_special_symbols_right >= 6 or 10 > num_of_special_symbols_left >= 6:
            print(f'ticket "{ticket}" - {min(num_of_special_symbols_left,num_of_special_symbols_right)}^')
        elif num_of_special_symbols_left == 10 and num_of_special_symbols_right == 10:
            print(f'ticket "{ticket}" - {num_of_special_symbols_right}^ Jackpot!')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print(f'ticket "{ticket}" - no match')
