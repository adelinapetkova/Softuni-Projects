class Software:
    name: str
    software_type: str
    capacity_consumption: int
    memory_consumption: int

    def __init__(self, name: str, software_type: str, capacity_consumption: int, memory_consumption: int):
        self.memory_consumption = memory_consumption
        self.software_type = software_type
        self.capacity_consumption = capacity_consumption
        self.name = name


