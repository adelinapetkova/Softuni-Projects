from class_and_static_methods.exercise.gym.customer import Customer
from class_and_static_methods.exercise.gym.equipment import Equipment
from class_and_static_methods.exercise.gym.exercise_plan import ExercisePlan
from class_and_static_methods.exercise.gym.subscription import Subscription
from class_and_static_methods.exercise.gym.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = None
        customer = None
        trainer = None
        equipment = None
        plan = None

        for sub in self.subscriptions:
            if sub.id == subscription_id:
                subscription = sub

        for cst in self.customers:
            if cst.id == subscription.customer_id:
                customer = cst

        for trn in self.trainers:
            if trn.id == subscription.trainer_id:
                trainer = trn

        for pl in self.plans:
            if pl.id == subscription.exercise_id:
                plan = pl

        for eqp in self.equipment:
            if eqp.id == plan.equipment_id:
                equipment = eqp

        result = ''
        result += str(subscription)
        result += '\n'
        result += str(customer)
        result += '\n'
        result += str(trainer)
        result += '\n'
        result += str(equipment)
        result += '\n'
        result += str(plan)

        return result
