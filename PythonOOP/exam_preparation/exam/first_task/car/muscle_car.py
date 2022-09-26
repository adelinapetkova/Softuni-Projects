from exam.first_task.car.car import Car


class MuscleCar(Car):
    MIN_SPEED_LIMIT = 250
    MAX_SPEED_LIMIT = 450
    car_type = "MuscleCar"

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

