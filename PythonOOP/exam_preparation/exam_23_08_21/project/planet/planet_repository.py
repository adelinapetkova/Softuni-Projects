from exam_preparation.exam_23_08_21.project.planet.planet import Planet


class PlanetRepository:
    planets: list

    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        self.planets.remove(planet)

    def find_by_name(self, name: str):
        for p in self.planets:
            if p.name == name:
                return p

