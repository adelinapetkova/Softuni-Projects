from exam_preparation.exam_10_04_21.project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    __AQUARIUM_TYPE = "SaltwaterAquarium"

    def __init__(self, name: str):
        super().__init__(name, 25)
