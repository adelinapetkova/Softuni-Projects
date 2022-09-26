from exam_preparation.exam_22_08.project.appliances.fridge import Fridge
from exam_preparation.exam_22_08.project.appliances.laptop import Laptop
from exam_preparation.exam_22_08.project.appliances.tv import TV
from exam_preparation.exam_22_08.project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        self.room_cost = 30
        tv = TV()
        laptop = Laptop()
        fridge = Fridge()
        gadgets = [tv, fridge, laptop]
        self.children = [ch for ch in children]
        self.appliances = gadgets * (2 + len(self.children))
        self.expenses_objects = [self.appliances]
        self.expenses_objects.append(self.children)
        self.calculate_expenses(*self.expenses_objects)
        super().__init__(family_name, salary_one + salary_two, 2 + len(self.children))
