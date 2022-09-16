from class_and_static_methods.exercise.animals.cat import Cat


class Kitten(Cat):
    def __init__(self, name: str, age):
        super().__init__(name, age, gender="Female")

    def make_sound(self):
        return "Meow"

