from exam_preparation.exam_10_04_21.project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    __DECORATION_TYPE = "Ornament"

    def __init__(self):
        super().__init__(1, 5.0)
