from exam_preparation.exam_23_08_21.project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    __OXYGEN_CONSUMPTION = 15

    def __init__(self, name: str):
        super().__init__(name, 90)

    def breathe(self):
        self.oxygen -= self.__OXYGEN_CONSUMPTION
