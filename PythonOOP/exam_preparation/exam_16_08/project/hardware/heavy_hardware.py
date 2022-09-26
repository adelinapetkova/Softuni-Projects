from exam_preparation.exam_16_08.project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Heavy", capacity*2, int(memory*75/100))
