from exam_preparation.exam_16_08.project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Power", int(capacity * 25 / 100), int(memory * 175 / 100))

