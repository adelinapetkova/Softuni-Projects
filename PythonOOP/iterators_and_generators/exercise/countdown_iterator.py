class countdown_iter:
    def __init__(self, count:int):
        self.count = count

    def __iter__(self):
        return countdown_iterator(self)


class countdown_iterator:
    def __init__(self, countdown_iter:countdown_iter):
        self.countdown_iter = countdown_iter
        self.value_to_return = self.countdown_iter.count + 1

    def __next__(self):
        self.value_to_return-=1
        if self.value_to_return==-1:
            raise StopIteration
        return self.value_to_return


iterator = countdown_iter(10)
for item in iterator:
    print(item, end= " ")


