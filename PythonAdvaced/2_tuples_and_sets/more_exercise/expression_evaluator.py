from collections import deque
from math import floor

expression = deque(input().split())
numbers = []

while len(expression)>0:
    element = expression.popleft()
    if element == '+':
        result = sum(numbers)
        numbers = []
        expression.appendleft(result)
    elif element == '-':
        result = numbers[0]
        for i in range(1, len(numbers)):
            result -= numbers[i]
        expression.appendleft(result)
        numbers = []
    elif element == '*':
        result = numbers[0]
        for i in range(1, len(numbers)):
            result *= numbers[i]
        expression.appendleft(result)
        numbers = []
    elif element == '/':
        result = numbers[0]
        for i in range(1, len(numbers)):
            result /= numbers[i]
        result = floor(result)
        expression.appendleft(result)
        numbers=[]
    else:
        element = int(element)
        numbers.append(element)

print(result)
