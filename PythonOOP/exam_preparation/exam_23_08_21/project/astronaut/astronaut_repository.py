from exam_preparation.exam_23_08_21.project.astronaut.astronaut import Astronaut


class AstronautRepository:
    astronauts: list

    def __init__(self):
        self.astronauts=[]

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for a in self.astronauts:
            if a.name==name:
                return a

    def astronaut_info(self):
        result=""
        for a in self.astronauts:
            if not a.backpack:
                items="none"
            else:
                items=", ".join(a.backpack)

            info=f"Name: {a.name}\n" \
                 f"Oxygen: {a.oxygen}\n" \
                 f"Backpack items: {items}\n"

            result+=info

        return result

