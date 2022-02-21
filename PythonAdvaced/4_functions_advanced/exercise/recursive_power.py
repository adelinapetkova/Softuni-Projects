def recursive_power(base, power, index=0, result=1):
    if index==power:
        return result
    result*=base
    return recursive_power(base, power, index+1, result)


print(recursive_power(10, 100, 0, 1))
