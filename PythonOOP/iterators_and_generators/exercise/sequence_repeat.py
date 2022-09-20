class sequence_repeat:
    def __init__(self, text, number):
        self.number = number
        self.text = text

    def __iter__(self):
        return sequence_repeat_iterator(self)


class sequence_repeat_iterator:
    def __init__(self, sequence_repeat: sequence_repeat):
        self.sequence_repeat = sequence_repeat
        self.iterations = 0

    def __next__(self):
        if self.iterations == self.sequence_repeat.number:
            raise StopIteration

        self.iterations += 1
        if self.iterations > len(self.sequence_repeat.text):
            index_of_letter_to_return = self.iterations % len(self.sequence_repeat.text) - 1
        else:
            index_of_letter_to_return = self.iterations - 1

        return self.sequence_repeat.text[index_of_letter_to_return]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

print()

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
