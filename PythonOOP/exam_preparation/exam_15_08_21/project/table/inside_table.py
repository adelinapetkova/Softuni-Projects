from exam_preparation.exam_15_08_21.project.table.table import Table


class InsideTable(Table):
    __MAX_TABLE_NUMBER = 50
    __MIN_TABLE_NUMBER = 1
    __INVALID_TABLE_NUMBER_MESSAGE = "Inside table's number must be between 1 and 50 inclusive!"

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)
