from abc import ABC, abstractmethod


class BakedFood(ABC):
    name: str
    portion: float
    price: float

    @abstractmethod
    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.price = price
        self.portion = portion

    @staticmethod
    def __validate_name(value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty string or white space!")

    @staticmethod
    def __validate_price(value):
        if value<=0:
            raise ValueError("Price cannot be less than or equal to zero!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name=value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__validate_price(value)
        self.__price=value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"

