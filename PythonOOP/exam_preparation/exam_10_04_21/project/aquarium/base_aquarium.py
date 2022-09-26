from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    __AQUARIUM_TYPE = None
    name: str
    capacity: int
    decorations: list
    fish: list

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @staticmethod
    def __validate_name(value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    def add_fish(self, fish):
        if self.capacity==len(self.fish):
            return "Not enough capacity."

        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for f in self.fish:
            f.eat()

    def __str__(self):
        if not self.fish:
            names_fish="none"
        else:
            names_fish=" ".join([f.name for f in self.fish])

        return f"{self.name}:\n" \
               f"Fish: {names_fish}\n" \
               f"Decorations: {len(self.decorations)}\n" \
               f"Comfort: {self.calculate_comfort()}\n"
