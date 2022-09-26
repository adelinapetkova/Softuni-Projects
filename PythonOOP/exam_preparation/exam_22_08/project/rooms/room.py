class Room:
    family_name: str
    budget: float
    members_count: int
    children = []
    appliances = []
    expenses = 0
    room_cost = 0

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count

    def calculate_expenses(self, *args):
        for elements_list in args:
            for element in elements_list:
                self.expenses += element.get_monthly_expense()
