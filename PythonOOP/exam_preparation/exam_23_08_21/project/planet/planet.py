class Planet:
    name: str
    items: list

    def __init__(self, name: str):
        self.name = name
        self.items = []

    @staticmethod
    def __validate_name(value):
        if not value or not value.strip():
            raise ValueError("Planet name cannot be empty string or whitespace!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value
