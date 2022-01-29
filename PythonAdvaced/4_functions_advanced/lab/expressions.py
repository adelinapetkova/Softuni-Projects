def generating_expressions(signs, expression_with_signs, index, nums):
    if len(expression_with_signs) == len(nums):
        result = 0
        expression = ''
        for i in range(len(expression_with_signs)):
            expression += expression_with_signs[i]
            expression += nums[i]
            if expression_with_signs[i] == '+':
                result += int(nums[i])
            elif expression_with_signs[i] == '-':
                result -= int(nums[i])
        print(f'{expression}={result}')
        return
    for i in range(len(signs)):
        expression_with_signs.append(signs[i])
        generating_expressions(signs, expression_with_signs, index, nums)
        expression_with_signs.pop()


signs_list = ['+', '-']
numbers = input().split(', ')
generating_expressions(signs_list, [], 0, numbers)
