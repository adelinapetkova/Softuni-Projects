from exam_preparation.exam_22_08.project.appliances.tv import TV
from exam_preparation.exam_22_08.project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, 1)
        self.room_cost = 10
        tv=TV()
        self.appliances=[tv]
        self.objects=[self.appliances]
        self.calculate_expenses(*self.objects)

