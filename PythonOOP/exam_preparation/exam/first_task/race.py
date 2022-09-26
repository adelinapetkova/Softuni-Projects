class Race:
    name: str
    drivers: list

    def __init__(self, name: str):
        self.name = name
        self.drivers = []

    @staticmethod
    def __validate_name(value):
        if not value:
            raise ValueError("Name cannot be an empty string!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    def find_winners(self):
        driver_speed_dict = {}
        for driver in self.drivers:
            driver_speed_dict[driver.name] = driver.car.speed_limit

        sorted_driver_speed_dict = dict(sorted(driver_speed_dict.items(), key=lambda x: -x[1]))
        winners = []

        for key, value in sorted_driver_speed_dict.items():
            for d in self.drivers:
                if d.name == key:
                    winners.append(d)

            if len(winners) == 3:
                break

        return winners
