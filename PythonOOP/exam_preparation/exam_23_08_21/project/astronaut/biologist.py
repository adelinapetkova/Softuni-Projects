from exam_preparation.exam_23_08_21.project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    __OXYGEN_CONSUMPTION = 5

    def __init__(self, name: str):
        super().__init__(name, 70)

    def breathe(self):
        self.oxygen -= self.__OXYGEN_CONSUMPTION
