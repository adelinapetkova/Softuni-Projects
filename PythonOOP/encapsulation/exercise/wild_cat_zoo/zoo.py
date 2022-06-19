class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.__workers_capacity = workers_capacity
        self.__animal_capacity = animal_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        elif self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        money_for_workers = 0
        for worker in self.workers:
            money_for_workers += worker.salary

        if self.__budget < money_for_workers:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= money_for_workers
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        money_for_animals_care = 0
        for animal in self.animals:
            money_for_animals_care += animal.money_for_care

        if self.__budget < money_for_animals_care:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= money_for_animals_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals_dict = {"Lions": [], "Tigers": [], "Cheetahs": []}
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                animals_dict["Lions"].append(animal.__repr__())
            elif animal.__class__.__name__ == "Tiger":
                animals_dict["Tigers"].append(animal.__repr__())
            elif animal.__class__.__name__ == "Cheetah":
                animals_dict["Cheetahs"].append(animal.__repr__())

        info = [f"You have {len(self.animals)} animals"]
        for key, value in animals_dict.items():
            info.append(f"----- {len(value)} {key}:")
            for animal in value:
                info.append(animal)

        return "\n".join(info)

    def workers_status(self):
        workers_dict = {"Keepers": [], "Caretakers": [], "Vets": []}
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                workers_dict["Keepers"].append(worker.__repr__())
            elif worker.__class__.__name__ == "Caretaker":
                workers_dict["Caretakers"].append(worker.__repr__())
            elif worker.__class__.__name__ == "Vet":
                workers_dict["Vets"].append(worker.__repr__())

        info=[f"You have {len(self.workers)} workers"]
        for key, value in workers_dict.items():
            info.append(f"----- {len(value)} {key}:")
            for worker in value:
                info.append(worker)

        return "\n".join(info)

