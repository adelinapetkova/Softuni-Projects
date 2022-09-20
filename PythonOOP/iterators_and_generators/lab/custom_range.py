class custom_range:
    def __init__(self, start:int, end:int, step=1):
        self.step = step
        self.end = end
        self.start = start

    def __iter__(self):
        return custom_range_iterator(self)


class custom_range_iterator:
    def __init__(self, custom_range:custom_range):
        self.custom_range = custom_range
        self.number_to_return=custom_range.start-1
        self.step=custom_range.step

    def __next__(self):
        self.number_to_return+=self.step
        if self.step>0 and self.number_to_return>self.custom_range.end:
            raise StopIteration

        return self.number_to_return


numbers_range=custom_range(1, 10)
for num in numbers_range:
    print(num)
