from exam_preparation.exam_15_08_21.project.drink.drink import Drink


class Tea(Drink):
    def __init__(self, name, portion, brand):
        super().__init__(name, portion, 2.50, brand)
