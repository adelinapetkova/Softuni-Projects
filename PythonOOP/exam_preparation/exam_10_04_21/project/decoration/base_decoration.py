from abc import ABC, abstractmethod


class BaseDecoration(ABC):
    __DECORATION_TYPE=None
    comfort: int
    price: float

    @abstractmethod
    def __init__(self, comfort, price):
        self.comfort = comfort
        self.price = price
