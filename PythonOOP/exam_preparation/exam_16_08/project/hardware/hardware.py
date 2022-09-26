from exam_preparation.exam_16_08.project.software.software import Software


class Hardware:
    name: str
    hardware_type: str
    capacity: int
    memory: int
    software_components: list

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.memory = memory
        self.capacity = capacity
        self.hardware_type = hardware_type
        self.name = name
        self.software_components = []

    def install(self, software: Software):
        if self.capacity >= software.capacity_consumption and self.memory >= software.memory_consumption:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
