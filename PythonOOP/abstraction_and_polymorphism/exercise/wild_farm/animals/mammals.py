from polymorphism_and_abstraction.exercise.wild_farm.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOODS = ["Vegetable", "Fruit"]
    WEIGHT_MULTIPLIER = 0.10

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    ALLOWED_FOODS = ["Meat"]
    WEIGHT_MULTIPLIER = 0.40

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    ALLOWED_FOODS = ["Meat", "Vegetable"]
    WEIGHT_MULTIPLIER = 0.30

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    ALLOWED_FOODS = ["Meat"]
    WEIGHT_MULTIPLIER = 1.00

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"


