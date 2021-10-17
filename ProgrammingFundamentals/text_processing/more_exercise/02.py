first_char_ascii=ord(input())
second_char_ascii=ord(input())

text=input()
total=0

for el in text:
    if first_char_ascii<ord(el)<second_char_ascii:
        total+=ord(el)

print(total)