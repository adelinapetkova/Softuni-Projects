number=int(input())


for i in range(1111,9999):
    i_as_string=str(i)
    is_special_number=True
    for index, digit in enumerate(i_as_string):
        if int(digit)==0:
            is_special_number=False
            break
        elif number % int(digit) != 0:
            is_special_number=False
            break
    if is_special_number:
        print(i, end=' ')