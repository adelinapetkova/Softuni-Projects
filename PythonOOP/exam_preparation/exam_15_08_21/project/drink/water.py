from exam_preparation.exam_15_08_21.project.drink.drink import Drink


class Water(Drink):
    def __init__(self, name, portion, brand):
        super().__init__(name, portion, 1.50, brand)
