def smallest(num_1,num_2,num_3):
    smallest_number=num_1
    if num_2<smallest_number:
        smallest_number=num_2
    if num_3<smallest_number:
        smallest_number=num_3
    return smallest_number

number_1=int(input())
number_2=int(input())
number_3=int(input())

print(smallest(number_1,number_2,number_3))
