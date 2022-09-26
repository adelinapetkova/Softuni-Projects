from abc import ABC, abstractmethod


class Astronaut(ABC):
    __OXYGEN_CONSUMPTION=10
    name: str
    oxygen: int
    backpack: list

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @staticmethod
    def __validate_name(value):
        if not value or not value.strip():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @abstractmethod
    def breathe(self):
        self.oxygen -= self.__OXYGEN_CONSUMPTION

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
