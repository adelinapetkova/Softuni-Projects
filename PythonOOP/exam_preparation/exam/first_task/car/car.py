from abc import ABC, abstractmethod


class Car(ABC):
    MIN_SPEED_LIMIT: None
    MAX_SPEED_LIMIT: None
    car_type: None
    model: str
    speed_limit: int
    is_taken: bool

    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @staticmethod
    def __validate_model(value):
        if not value or len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")

    @classmethod
    def __validate_speed_limit(cls, value):
        if not cls.MIN_SPEED_LIMIT <= value <= cls.MAX_SPEED_LIMIT:
            raise ValueError(
                f"Invalid speed limit! Must be between {cls.MIN_SPEED_LIMIT} and {cls.MAX_SPEED_LIMIT}!")

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__validate_model(value)
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        self.__validate_speed_limit(value)
        self.__speed_limit = value
