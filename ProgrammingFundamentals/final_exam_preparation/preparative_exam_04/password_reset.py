password=input()
command=input()

while not command=='Done':
    result=''
    if 'TakeOdd' in command:
        for i in range(0, len(password)):
            if i%2==1:
                result+=password[i]
        password=result
        print(password)
    elif 'Cut' in command:
        action, index, length=command.split()
        index=int(index)
        length=int(length)
        substring_to_remove=password[index:index+length]
        result=password.replace(substring_to_remove, '', 1)
        password=result
        print(password)
    elif 'Substitute' in command:
        action, substring, substitute=command.split()
        if substring in password:
            result=password.replace(substring,substitute)
            password=result
            print(password)
        else:
            print('Nothing to replace!')
    command=input()

print(f'Your password is: {password}')