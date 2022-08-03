from abc import ABC, abstractmethod
from polymorphism_and_abstraction.exercise.wild_farm.food import Food


class Animal(ABC):
    ALLOWED_FOODS = []
    WEIGHT_MULTIPLIER = 1

    def __init__(self, name: str, weight: float):
        self.weight = weight
        self.name = name
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        if food.__class__.__name__ not in self.ALLOWED_FOODS:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += self.WEIGHT_MULTIPLIER * food.quantity
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}," \
               f" {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}," \
               f" {self.living_region}, {self.food_eaten}]"
