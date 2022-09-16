from class_and_static_methods.exercise.movie_world.dvd import DVD
from class_and_static_methods.exercise.movie_world.customer import Customer


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer_who_wants_to_rent = None
        wanted_dvd = None
        for person in self.customers:
            if person.id == customer_id:
                customer_who_wants_to_rent = person

        for dvd in self.dvds:
            if dvd.id == dvd_id:
                wanted_dvd = dvd

        if wanted_dvd.is_rented:
            for dvd in customer_who_wants_to_rent.rented_dvds:
                if dvd == wanted_dvd:
                    return f"{customer_who_wants_to_rent.name} has already rented {wanted_dvd.name}"

            return "DVD is already rented"

        if customer_who_wants_to_rent.age < wanted_dvd.age_restriction:
            return f"{customer_who_wants_to_rent.name} should be at least " \
                   f"{wanted_dvd.age_restriction} to rent this movie"

        wanted_dvd.is_rented = True
        customer_who_wants_to_rent.rented_dvds.append(wanted_dvd)
        return f"{customer_who_wants_to_rent.name} has successfully rented {wanted_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer_who_wants_to_return = None
        dvd_to_return = None
        for person in self.customers:
            if person.id == customer_id:
                customer_who_wants_to_return = person

        for dvd in self.dvds:
            if dvd.id == dvd_id:
                dvd_to_return = dvd

        if dvd_to_return in customer_who_wants_to_return.rented_dvds:
            customer_who_wants_to_return.rented_dvds.remove(dvd_to_return)
            dvd_to_return.is_rented = False
            return f"{customer_who_wants_to_return.name} has successfully returned {dvd_to_return.name}"

        return f"{customer_who_wants_to_return.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for c in self.customers:
            result += str(c)
            result += '\n'

        for d in self.dvds:
            result += str(d)
            result += '\n'

        return result.strip()
