file='my_first_file.txt'
text='I just created my first file'

with open(file, 'w') as files:
    files.write(text)

file1=open('my_second_file.txt', 'w')
file1.write('I just created my second file')