from exam_preparation.exam_10_04_21.project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    __AQUARIUM_TYPE = "FreshwaterAquarium"

    def __init__(self, name: str):
        super().__init__(name, 50)
