from exam_preparation.exam_22_08.project.rooms.room import Room


class Everland:
    rooms: list

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses
            total_consumption += room.room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = ""
        for room in self.rooms:
            if room.budget - (room.expenses + room.room_cost) >= 0:
                room.budget -= room.expenses + room.room_cost
                result += f"{room.family_name} paid {(room.expenses + room.room_cost):.2f}$ and have {room.budget:.2f}$ left."
                result += "\n"
            else:
                self.rooms.remove(room)
                result += f"{room.family_name} does not have enough budget and must leave the hotel."
                result += "\n"

        return result

    def status(self):
        result = ""

        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            for i in range(0, len(room.children)):
                result += f"--- Child {i + 1} monthly cost: {room.children[i].get_monthly_expense():.2f}$\n"
            total_cost_for_appliances = 0
            for appliance in room.appliances:
                if isinstance(appliance, list) or isinstance(appliance, tuple):
                    for el in appliance:
                        total_cost_for_appliances += el.get_monthly_expense()
                else:
                    total_cost_for_appliances += appliance.get_monthly_expense()
            if total_cost_for_appliances > 0:
                result += f"--- Appliances monthly cost: {total_cost_for_appliances:.2f}$\n"

        total_population = 0
        for room in self.rooms:
            total_population += room.members_count
        result = f"Total population: {total_population}\n" + result

        return result
