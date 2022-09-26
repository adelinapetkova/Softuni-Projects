from exam_preparation.exam_15_08_21.project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    def __init__(self, name: str, price: float):
        super().__init__(name, 200, price)
