from abc import ABC, abstractmethod

from exam_preparation.exam_15_08_21.project.baked_food.baked_food import BakedFood
from exam_preparation.exam_15_08_21.project.drink.drink import Drink


class Table(ABC):
    __MIN_TABLE_NUMBER = None
    __MAX_TABLE_NUMBER = None
    __INVALID_TABLE_NUMBER_MESSAGE = None

    table_number: int
    capacity: int
    food_orders: list
    drink_orders: list
    number_of_people: int
    is_reserved: bool

    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @staticmethod
    def __validate_capacity(value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")

    @classmethod
    def __validate_table_number(cls, value):
        if cls.__MIN_TABLE_NUMBER and value < cls.__MIN_TABLE_NUMBER:
            raise ValueError(cls.__INVALID_TABLE_NUMBER_MESSAGE)

        if cls.__MAX_TABLE_NUMBER and cls.__MAX_TABLE_NUMBER < value:
            raise ValueError(cls.__INVALID_TABLE_NUMBER_MESSAGE)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__validate_capacity(value)
        self.__capacity = value

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        self.__validate_table_number(value)
        self.__table_number = value

    def reserve(self, number_of_people: int):
        if number_of_people <= self.capacity:
            self.number_of_people = number_of_people
            self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        total = 0
        for f in self.food_orders:
            total += f.price

        for d in self.drink_orders:
            total += d.price

        return total

    def clear(self):
        self.drink_orders = []
        self.food_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\n" \
                   f"Type: {self.__class__.__name__}\n" \
                   f"Capacity: {self.capacity}\n"
