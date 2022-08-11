class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.horse_power = horse_power
        self.fuel = fuel
        self.fuel_consumption=Vehicle.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: int):
        needed_fuel = kilometers * self.fuel_consumption
        if needed_fuel <= self.fuel:
            self.fuel -= needed_fuel


