from inheritance.exercise.need_for_speed.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption=Motorcycle.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: int):
        super().drive(kilometers)


