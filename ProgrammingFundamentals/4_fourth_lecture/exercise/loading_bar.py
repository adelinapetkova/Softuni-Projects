number=int(input())

def loading_bar(num):
    n=int(num/10)
    dots=int(10-n)
    if num==100:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
    else:
        percentages='%'*n
        dot='.'*dots
        print(f'{num}% [{percentages}{dot}]')
        print('Still loading...')

loading_bar(number)