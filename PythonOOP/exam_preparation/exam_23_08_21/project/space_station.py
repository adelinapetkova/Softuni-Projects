from exam_preparation.exam_23_08_21.project.planet.planet_repository import PlanetRepository
from exam_preparation.exam_23_08_21.project.astronaut.astronaut_repository import AstronautRepository
from exam_preparation.exam_23_08_21.project.astronaut.biologist import Biologist
from exam_preparation.exam_23_08_21.project.astronaut.geodesist import Geodesist
from exam_preparation.exam_23_08_21.project.astronaut.meteorologist import Meteorologist
from exam_preparation.exam_23_08_21.project.planet.planet import Planet
from exam_preparation.exam_23_08_21.project.astronaut.astronaut import Astronaut


class SpaceStation:
    planet_repository: PlanetRepository
    astronaut_repository: AstronautRepository
    completed_missions = 0
    not_completed_missions = 0

    def __init__(self):
        self.astronaut_repository = AstronautRepository()
        self.planet_repository = PlanetRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut: Astronaut
        if astronaut_type == "Biologist":
            astronaut = Biologist(name)
        elif astronaut_type == "Geodesist":
            astronaut = Geodesist(name)
        elif astronaut_type == "Meteorologist":
            astronaut = Meteorologist(name)
        else:
            raise Exception("Astronaut type is not valid!")

        if not self.astronaut_repository.find_by_name(name):
            self.astronaut_repository.add(astronaut)
            return f"Successfully added {astronaut_type}: {name}."
        else:
            return f"{name} is already added."

    def add_planet(self, name: str, items: str):
        planet = Planet(name)
        planet.items = items.split(", ")
        if not self.planet_repository.find_by_name(name):
            self.planet_repository.add(planet)
            return f"Successfully added Planet: {name}."
        else:
            return f"{name} is already added."

    def retire_astronaut(self, name: str):
        if not self.astronaut_repository.find_by_name(name):
            raise Exception(f"Astronaut {name} doesn't exist!")
        else:
            astronaut_to_remove = self.astronaut_repository.find_by_name(name)
            self.astronaut_repository.remove(astronaut_to_remove)
            return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        if not self.planet_repository.find_by_name(planet_name):
            raise Exception("Invalid planet name!")

        planet = self.planet_repository.find_by_name(planet_name)

        suitable_astronauts = []
        for a in self.astronaut_repository.astronauts:
            if a.oxygen > 30:
                suitable_astronauts.append(a)

        while len(suitable_astronauts) > 5:
            astronaut_to_remove = suitable_astronauts[0]
            for a in suitable_astronauts:
                if a.oxygen < astronaut_to_remove.oxygen:
                    astronaut_to_remove = a

            suitable_astronauts.remove(astronaut_to_remove)

        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        participated_astronauts = []
        while planet.items:
            current_explorer = suitable_astronauts[0]
            for a in suitable_astronauts:
                if a.oxygen > current_explorer.oxygen:
                    current_explorer = a

            while current_explorer.oxygen >= current_explorer.__OXYGEN_CONSUMPTION:
                if planet.items:
                    current_explorer.breathe()
                    current_explorer.backpack.append(planet.items.pop())
                else:
                    break

            participated_astronauts.append(current_explorer)

            no_more_oxygen = True
            for a in suitable_astronauts:
                if a.oxygen >= a.__OXYGEN_CONSUMPTION:
                    no_more_oxygen = False

            if no_more_oxygen:
                break

        if planet.items:
            self.not_completed_missions += 1
            return "Mission is not completed."
        else:
            self.completed_missions += 1
            return f"Planet: {planet_name} was explored. {len(participated_astronauts)} astronauts participated in " \
                   f"collecting items. "

    def report(self):
        result = ""
        result += f"{self.completed_missions} successful missions!\n"
        result += f"{self.not_completed_missions} missions were not completed!\n"
        result += "Astronauts' info:\n"
        result += self.astronaut_repository.astronaut_info()

        return result
