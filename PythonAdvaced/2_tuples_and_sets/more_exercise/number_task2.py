sequence_one={num for num in input().split()}
sequence_two={num for num in input().split()}

sequence_one=list(sequence_one)
sequence_two=list(sequence_two)

n=int(input())

for _ in range(n):
    action, sequence_number, *numbers = input().split()
    if action=='Add':
        if sequence_number=='First':
            for num in numbers:
                if num not in sequence_one:
                    sequence_one.append(num)
        else:
            for num in numbers:
                if num not in sequence_two:
                    sequence_two.append(num)
    elif action=='Remove':
        if sequence_number=='First':
            for num in numbers:
                if num in sequence_one:
                    sequence_one.remove(num)
        else:
            for num in numbers:
                if num in sequence_two:
                    sequence_two.remove(num)
    else:
        sequence_one=sorted(sequence_one)
        sequence_two=sorted(sequence_two)
        sequence_one_string=' '.join(sequence_one)
        sequence_two_string=' '.join(sequence_two)
        if sequence_one_string in sequence_two_string or sequence_two_string in sequence_one_string:
            print('True')
        else:
            print('False')

sequence_one=[int(x) for x in sequence_one]
sequence_two=[int(y) for y in sequence_two]

sequence_one=sorted(sequence_one)
sequence_two=sorted(sequence_two)

sequence_one=[str(x) for x in sequence_one]
sequence_two=[str(y) for y in sequence_two]

print(', '.join(sequence_one))
print(', '.join(sequence_two))