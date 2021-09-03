n=int(input())
l=int(input())
alphabet='abcdefghijklmnopqrstuvwxyz'


for symbol1 in range(1,n+1):
    for symbol2 in range(1,n+1):
        for index, letter in enumerate(alphabet):
            if index<l:
                symbol3=letter
                for count, symbol in enumerate(alphabet):
                    if count<l:
                        symbol4=symbol
                        for symbol5 in range(1,n+1):
                           if symbol5>symbol2 and symbol5>symbol1:
                             print(f'{symbol1}{symbol2}{symbol3}{symbol4}{symbol5}', end=' ')

