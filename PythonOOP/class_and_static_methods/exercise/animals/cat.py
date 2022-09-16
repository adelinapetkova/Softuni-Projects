from class_and_static_methods.exercise.animals.animal import Animal


class Cat(Animal):
    def __init__(self, name: str, age, gender: str):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Meow meow!"
