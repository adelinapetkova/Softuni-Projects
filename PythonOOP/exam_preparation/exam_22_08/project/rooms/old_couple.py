from exam_preparation.exam_22_08.project.appliances.fridge import Fridge
from exam_preparation.exam_22_08.project.appliances.stove import Stove
from exam_preparation.exam_22_08.project.appliances.tv import TV
from exam_preparation.exam_22_08.project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one + pension_two, 2)
        self.room_cost = 15
        tv = TV()
        stove = Stove()
        fridge = Fridge()
        self.appliances = [tv, stove, fridge, tv, stove, fridge]
        self.objects = [self.appliances]
        self.calculate_expenses(*self.objects)
