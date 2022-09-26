from exam_preparation.exam_10_04_21.project.decoration.decoration_repository import DecorationRepository
from exam_preparation.exam_10_04_21.project.aquarium.freshwater_aquarium import FreshwaterAquarium
from exam_preparation.exam_10_04_21.project.aquarium.saltwater_aquarium import SaltwaterAquarium
from exam_preparation.exam_10_04_21.project.decoration.ornament import Ornament
from exam_preparation.exam_10_04_21.project.decoration.plant import Plant
from exam_preparation.exam_10_04_21.project.fish.freshwater_fish import FreshwaterFish
from exam_preparation.exam_10_04_21.project.fish.saltwater_fish import SaltwaterFish


class Controller:
    decorations_repository: DecorationRepository
    aquariums: list

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "FreshwaterAquarium":
            aquarium = FreshwaterAquarium(aquarium_name)
        elif aquarium_type == "SaltwaterAquarium":
            aquarium = SaltwaterAquarium(aquarium_name)
        else:
            return "Invalid aquarium type."

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            decoration = Ornament()
        elif decoration_type == "Plant":
            decoration = Plant()
        else:
            return "Invalid decoration type."

        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        if aquarium_name in [a.name for a in self.aquariums]:
            aq = None
            for a in self.aquariums:
                if a.name == aquarium_name:
                    aq = a
            if self.decorations_repository.find_by_type(decoration_type):
                d = self.decorations_repository.find_by_type(decoration_type)
                self.decorations_repository.remove(d)
                aq.add_decoration(d)
                return f"Successfully added {decoration_type} to {aquarium_name}."
            else:
                return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
            fish_aquarium_type="FreshwaterAquarium"
        elif fish_type == "SaltwaterFish":
            fish = SaltwaterFish(fish_name, fish_species, price)
            fish_aquarium_type = "SaltwaterAquarium"
        else:
            return f"There isn't a fish of type {fish_type}."

        for aq in self.aquariums:
            if aq.name == aquarium_name:
                if aq.__class__.__name__ == fish_aquarium_type:
                    aq.add_fish(fish)
                else:
                    return "Water not suitable."

    def feed_fish(self, aquarium_name: str):
        for aq in self.aquariums:
            if aq.name == aquarium_name:
                aq.feed()
                return f"Fish fed: {len(aq.fish)}"

    def calculate_value(self, aquarium_name: str):
        total_value = 0
        for aq in self.aquariums:
            if aq.name == aquarium_name:
                total_value += sum([f.price for f in aq.fish])
                total_value += sum([d.price for d in aq.decorations])

        return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."

    def report(self):
        result=""
        for aq in self.aquariums:
            result+=aq.__str__

        return result
