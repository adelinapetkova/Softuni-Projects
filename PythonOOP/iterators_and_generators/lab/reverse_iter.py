class reverse_iter:
    def __init__(self, iterable):
        self.iterable = list(iterable)

    def __iter__(self):
        return reverse_iterator(self)


class reverse_iterator:
    def __init__(self, reverse_iter):
        self.reverse_iter = reverse_iter
        self.index_of_number_to_return = 0

    def __next__(self):
        self.index_of_number_to_return+=-1
        try:
            return self.reverse_iter.iterable[self.index_of_number_to_return]
        except IndexError:
            raise StopIteration


reversed_list = reverse_iter({1, 2, 3, 4})
for item in reversed_list:
    print(item)
