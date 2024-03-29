from inheritance.exercise.need_for_speed.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self,fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption=8

    def drive(self, kilometers: int):
        super().drive(kilometers)
