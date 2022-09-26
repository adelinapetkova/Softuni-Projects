from exam_preparation.exam_22_08.project.appliances.fridge import Fridge
from exam_preparation.exam_22_08.project.appliances.laptop import Laptop
from exam_preparation.exam_22_08.project.appliances.tv import TV
from exam_preparation.exam_22_08.project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 20
        tv = TV()
        laptop = Laptop()
        fridge = Fridge()
        self.appliances = [tv, laptop, fridge, tv, laptop, fridge]
        self.objects = [self.appliances]
        self.calculate_expenses(*self.objects)
