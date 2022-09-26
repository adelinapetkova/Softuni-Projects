from exam_preparation.exam_10_04_21.project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    __DECORATION_TYPE = "Plant"

    def __init__(self):
        super().__init__(5, 10.0)
