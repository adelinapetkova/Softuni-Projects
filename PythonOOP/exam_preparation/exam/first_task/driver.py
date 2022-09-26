from exam.first_task.car import Car


class Driver:
    name: str
    car: Car
    number_of_wins: int

    def __init__(self, name: str):
        self.name = name
        self.car=None
        self.number_of_wins = 0

    @staticmethod
    def __validate_name(value):
        if not value or not value.strip():
            raise ValueError("Name should contain at least one character!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value
