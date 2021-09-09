class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals+=1

    def get_info(self, species):
        if species == 'mammal':
            return f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == 'fish':
            return f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == 'bird':
            return f"Birds in {self.name}: {', '.join(self.birds)}"


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
n = int(input())

for _ in range(n):
    species, name = input().split(' ')
    zoo.add_animal(species, name)

species_for_print = input()

print(zoo.get_info(species_for_print))
print(f'Total animals: {n}')
