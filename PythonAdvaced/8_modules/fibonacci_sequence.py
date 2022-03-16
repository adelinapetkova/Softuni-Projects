def fibonacci_sequence(n):
    sequence=[0,1]
    n-=2
    for i in range(n):
        sum_to_add=sequence[len(sequence)-1]+sequence[len(sequence)-2]
        sequence.append(sum_to_add)

    return sequence


def locate(sequence, num_to_search):
    if num_to_search in sequence:
        index=sequence.index(num_to_search)
        return index
    return False

