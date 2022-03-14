import math
from math import log

number=int(input())
base=input()

if base=='natural':
    print(log(number, math.e))
else:
    base=int(base)
    print(log(number, base))