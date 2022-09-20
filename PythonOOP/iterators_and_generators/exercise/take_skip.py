class take_skip:
    def __init__(self, step:int, count:int):
        self.count = count
        self.step = step

    def __iter__(self):
        return take_skip_iterator(self)


class take_skip_iterator:
    def __init__(self, take_ship:take_skip):
        self.take_ship = take_ship
        self.number_to_return = 0
        self.iterations = 0

    def __next__(self):
        if self.iterations==self.take_ship.count:
            raise StopIteration

        value_to_return=self.number_to_return
        self.iterations+=1
        self.number_to_return+=self.take_ship.step
        return value_to_return


numbers = take_skip(10, 5)
for number in numbers:
    print(number)



