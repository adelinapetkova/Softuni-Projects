from exam.first_task.car import MuscleCar
from exam.first_task.car import SportsCar
from exam.first_task.driver import Driver
from exam.first_task.race import Race


class Controller:
    cars: list
    drivers: list
    races: list

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = None
        if car_type == "MuscleCar":
            car = MuscleCar(model, speed_limit)
        elif car_type == "SportsCar":
            car = SportsCar(model, speed_limit)

        if model in [c.model for c in self.cars]:
            raise Exception(f"Car {model} is already created!")

        if car:
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = Driver(driver_name)

        if driver_name in [d.name for d in self.drivers]:
            raise Exception(f"Driver {driver_name} is already created!")

        if driver:
            self.drivers.append(driver)
            return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = Race(race_name)

        if race_name in [r.name for r in self.races]:
            raise Exception(f"Race {race_name} is already created!")

        if race:
            self.races.append(race)
            return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = None
        car = None

        for d in self.drivers:
            if d.name == driver_name:
                driver = d

        for c in self.cars:
            if c.car_type == car_type and not c.is_taken:
                car = c

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car:
            driver.car.is_taken=False
            old_car_model = driver.car.model
            driver.car = car
            car.is_taken = True
            return f"Driver {driver.name} changed his car from {old_car_model} to {car.model}."

        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = None
        driver = None

        for r in self.races:
            if r.name == race_name:
                race = r

        for d in self.drivers:
            if d.name == driver_name:
                driver = d

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        else:
            race.drivers.append(driver)
            return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = None

        for r in self.races:
            if r.name == race_name:
                race = r

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = race.find_winners()
        result = ""

        for w in winners:
            w.number_of_wins += 1
            result += f"Driver {w.name} wins the {race_name} race with a speed of {w.car.speed_limit}.\n"

        return result
