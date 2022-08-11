from inheritance.exercise.need_for_speed.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption=10

    def drive(self, kilometers: int):
        super().drive(kilometers)


