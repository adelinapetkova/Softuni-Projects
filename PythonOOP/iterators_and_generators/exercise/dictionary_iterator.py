class dictionary_iter:
    def __init__(self, my_dictionary: dict):
        self.my_dictionary = my_dictionary

    def __iter__(self):
        return dictionary_iterator(self)


class dictionary_iterator:
    def __init__(self, dict_iter: dictionary_iter):
        self.dict_iter = dict_iter
        self.index = 1

    def __next__(self):
        iterations = 0
        for key, value in self.dict_iter.my_dictionary.items():
            iterations += 1
            if iterations == self.index:
                value_to_return = (key, value)
                self.index += 1
                return value_to_return
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
