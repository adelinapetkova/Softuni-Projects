from exam_preparation.exam_16_08.project.hardware.heavy_hardware import HeavyHardware
from exam_preparation.exam_16_08.project.hardware.power_hardware import PowerHardware
from exam_preparation.exam_16_08.project.software.light_software import LightSoftware
from exam_preparation.exam_16_08.project.software.express_software import ExpressSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware_name_exists = False
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                hardware_name_exists = True
                express = ExpressSoftware(name, capacity_consumption, memory_consumption)
                hardware.install(express)
                System._software.append(express)

        if not hardware_name_exists:
            return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware_name_exists = False
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                hardware_name_exists = True
                light = LightSoftware(name, capacity_consumption, memory_consumption)
                hardware.install(light)
                System._software.append(light)

        if not hardware_name_exists:
            return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware_in_system = False
        software_in_system = False
        software_to_uninstall = None

        for software in System._software:
            if software.name == software_name:
                software_in_system = True
                software_to_uninstall = software
                break

        for hardware in System._hardware:
            if hardware.name == hardware_name:
                hardware_in_system = True
                if software_in_system:
                    return hardware.software_components.remove(software_to_uninstall)
                break

        if hardware_in_system and software_in_system:
            System._software.remove(software_to_uninstall)

    @staticmethod
    def analyze():
        total_memory_hardware = 0
        total_capacity_hardware = 0
        total_memory_software = 0
        total_capacity_software = 0

        for hardware in System._hardware:
            total_memory_hardware += hardware.memory
            total_capacity_hardware += hardware.capacity

        for software in System._software:
            total_capacity_software += software.capacity_consumption
            total_memory_software += software.memory_consumption

        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {total_memory_software} / {total_memory_hardware}\n" \
               f"Total Capacity Taken: {total_capacity_software} / {total_capacity_hardware}"

    @staticmethod
    def system_split():
        result = ""
        for hardware in System._hardware:
            light_count = 0
            express_count = 0
            total_memory_used_by_software = 0
            total_capacity_used_by_software = 0
            names_of_software_components = []
            for software in hardware.software_components:
                names_of_software_components.append(software.name)
                total_memory_used_by_software += software.memory_consumption
                total_capacity_used_by_software += software.capacity_consumption
                if software.software_type == "Light":
                    light_count += 1
                elif software.software_type == "Express":
                    express_count += 1

            if names_of_software_components:
                names = ", ".join(names_of_software_components)
            else:
                names = "None"

            result += f"Hardware Component - {hardware.name}\n" \
                      f"Express Software Components: {express_count}\n" \
                      f"Light Software Components: {light_count}\n" \
                      f"Memory Usage: {total_memory_used_by_software} / {hardware.memory}\n" \
                      f"Capacity Usage: {total_capacity_used_by_software} / {hardware.capacity}\n" \
                      f"Type: {hardware.hardware_type}\n" \
                      f"Software Components: {names}\n"

        return result
