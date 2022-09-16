from abc import ABC,abstractmethod


class Animal(ABC):
    def __init__(self, name:str, age, gender:str):
        self.gender = gender
        self.age = age
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"
