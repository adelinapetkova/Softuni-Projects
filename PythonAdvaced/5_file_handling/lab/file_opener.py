file = open('/Users/adelinapetkova/PycharmProjects/pythonProject/file_handling/text.py', 'r')

nums_sum=0
for num in file.readlines():
    nums_sum+=int(num)

print(nums_sum)