from exam_preparation.exam_15_08_21.project.baked_food.cake import Cake
from exam_preparation.exam_15_08_21.project.baked_food.bread import Bread
from exam_preparation.exam_15_08_21.project.drink.tea import Tea
from exam_preparation.exam_15_08_21.project.drink.water import Water
from exam_preparation.exam_15_08_21.project.table.inside_table import InsideTable
from exam_preparation.exam_15_08_21.project.table.outside_table import OutsideTable


class Bakery:
    name: str
    food_menu: list
    drinks_menu: list
    tables_repository: list
    total_income: float

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @staticmethod
    def __validate_name(value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty string or white space!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name=value

    def add_food(self, food_type: str, name: str, price: float):
        food = None
        if food_type == "Bread":
            food = Bread(name, price)
        elif food_type == "Cake":
            food = Cake(name, price)

        for bf in self.food_menu:
            if bf.name == food.name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        if food:
            self.food_menu.append(food)
            return f"Added {food.name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        drink = None
        if drink_type == "Tea":
            drink = Tea(name, portion, brand)
        elif drink_type == "Water":
            drink = Water(name, portion, brand)

        for d in self.drinks_menu:
            if d.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink:
            self.drinks_menu.append(drink)
            return f"Added {drink.name} ({drink.brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table = None
        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)

        for t in self.tables_repository:
            if t.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        if table:
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for t in self.tables_repository:
            if not t.is_reserved:
                t.reserve(number_of_people)
                return f"Table {t.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        result_string = f"Table {table_number} ordered:\n"
        table = None
        foods_not_in_menu = []
        for t in self.tables_repository:
            if t.table_number == table_number:
                table = t

        if not table:
            return f"Could not find table {table_number}"

        for food in args:
            in_menu = False
            for f in self.food_menu:
                if f.name == food:
                    table.food_orders.append(f)
                    in_menu = True
                    result_string += f"{f.__repr__}\n"
            if not in_menu:
                foods_not_in_menu.append(food)

        result_string += f"{self.name} does not have in the menu:\n"
        for f in foods_not_in_menu:
            result_string += f"{f}\n"

        return result_string

    def order_drink(self, table_number: int, *args):
        result_string = f"Table {table_number} ordered:\n"
        table = None
        drinks_not_in_menu = []
        for t in self.tables_repository:
            if t.table_number == table_number:
                table = t

        if not table:
            return f"Could not find table {table_number}"

        for drink in args:
            in_menu = False
            for d in self.drinks_menu:
                if d.name == drink:
                    table.drink_orders.append(d)
                    in_menu = True
                    result_string += f"{d.__repr__}\n"
            if not in_menu:
                drinks_not_in_menu.append(drink)

        result_string += f"{self.name} does not have in the menu:\n"
        for f in drinks_not_in_menu:
            result_string += f"{f}\n"

        return result_string

    def leave_table(self, table_number: int):
        for t in self.tables_repository:
            if t.table_number == table_number:
                self.total_income += t.get_bill()
                return f"Table: {table_number}\n" \
                       f"Bill: {t.get_bill():.2f}\n"

    def get_free_tables_info(self):
        result = ""
        for t in self.tables_repository:
            result += t.free_table_info()

        return result

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
