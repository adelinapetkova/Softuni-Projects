def range_characters(char_1,char_2):
    for i in range(ord(char_1)+1,ord(char_2)):
        print(chr(i),end=' ')

start=input()
end=input()

range_characters(start,end)

