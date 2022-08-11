from inheritance.exercise.need_for_speed.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption=3

    def drive(self, kilometers: int):
        super().drive(kilometers)

