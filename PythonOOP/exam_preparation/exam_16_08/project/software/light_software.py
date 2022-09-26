from exam_preparation.exam_16_08.project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, "Light", int((capacity_consumption*150)/100), int(memory_consumption*50/100))
