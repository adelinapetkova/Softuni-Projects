from car_manager import Car

import unittest


class CarTests(unittest.TestCase):
    valid_make = 'make'
    valid_model = 'model'
    valid_fuel_consumption = 20
    valid_fuel_capacity = 40
    valid_fuel_amount = 0

    def test__init__with_valid_values__expect_correct_values_to_variables(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)

        self.assertEqual(self.valid_model, car.model)
        self.assertEqual(self.valid_make, car.make)
        self.assertEqual(self.valid_fuel_capacity, car.fuel_capacity)
        self.assertEqual(self.valid_fuel_consumption, car.fuel_consumption)

    def test__make_getter_expect_correct_value(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)

        self.assertEqual(car.make, self.valid_make)

    def test__make_setter__with_valid_new_value__expect_make_equal_to_new_value(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)
        car.make = "make_new"

        expected = "make_new"
        actual = car.make

        self.assertEqual(expected, actual)

    def test__make_setter__with_invalid_new_value__expect_exception(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)

        with self.assertRaises(Exception) as context:
            car.make = ''

        self.assertEqual(str(context.exception), "Make cannot be null or empty!")

    def test__model_getter_expect_correct_value(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)

        self.assertEqual(car.model, self.valid_model)

    def test__model_setter__with_valid_new_value__expect_make_equal_to_new_value(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)
        car.model = "model_new"

        expected = "model_new"
        actual = car.model

        self.assertEqual(expected, actual)

    def test__model_setter__with_invalid_new_value__expect_exception(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)

        with self.assertRaises(Exception) as context:
            car.model = ''

        self.assertEqual(str(context.exception), "Model cannot be null or empty!")

    def test__fuel_consumption_getter_expect_correct_value(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)

        self.assertEqual(car.fuel_consumption, self.valid_fuel_consumption)

    def test__fuel_consumption_setter__with_valid_new_value__expect_make_equal_to_new_value(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)
        car.fuel_consumption = 25

        expected = 25
        actual = car.fuel_consumption

        self.assertEqual(expected, actual)

    def test__fuel_consumption_setter__with_negative_new_value__expect_exception(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)

        with self.assertRaises(Exception) as context:
            car.fuel_consumption = -10

        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test__fuel_consumption_setter__with_zero_new_value__expect_exception(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)

        with self.assertRaises(Exception) as context:
            car.fuel_consumption = 0

        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test__fuel_capacity_getter_expect_correct_value(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)

        self.assertEqual(car.fuel_capacity, self.valid_fuel_capacity)

    def test__fuel_capacity_setter__with_valid_new_value__expect_make_equal_to_new_value(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)
        car.fuel_capacity = 35

        expected = 35
        actual = car.fuel_capacity

        self.assertEqual(expected, actual)

    def test__fuel_capacity_setter__with_negative_new_value__expect_exception(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)

        with self.assertRaises(Exception) as context:
            car.fuel_capacity = -20

        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test__fuel_capacity_setter__with_zero_new_value__expect_exception(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)

        with self.assertRaises(Exception) as context:
            car.fuel_capacity = 0

        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test__fuel_amount_getter__expect_correct_value(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)

        self.assertEqual(car.fuel_amount, self.valid_fuel_amount)

    def test__fuel_amount_setter__with_valid_values__expect_make_equal_to_new_value(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)
        car.fuel_amount = 40

        expected = 40
        actual = car.fuel_amount

        self.assertEqual(expected, actual)

    def test__fuel_amount_setter__with_valid_zero_value__expect_make_equal_to_new_value(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)
        car.fuel_amount = 0

        expected = 0
        actual = car.fuel_amount

        self.assertEqual(expected, actual)

    def test__fuel_amount_setter__with_negative_new_value__expect_exception(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)

        with self.assertRaises(Exception) as context:
            car.fuel_amount = -30

        self.assertEqual(str(context.exception), "Fuel amount cannot be negative!")

    def test__refuel__with_valid_value_less_than_capacity__expect_fuel_amount_equal_to_value(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)
        car.refuel(20)

        expected = 20
        actual = car.fuel_amount

        self.assertEqual(expected, actual)

    def test__refuel__with_valid_value_more_than_capacity__expect_fuel_amount_equal_to_capacity(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)
        car.refuel(50)

        expected = 40
        actual = car.fuel_amount

        self.assertEqual(expected, actual)

    def test__refuel__with_invalid_negative_value__expect_exception(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)

        with self.assertRaises(Exception) as context:
            car.refuel(-20)

        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test__refuel__with_invalid_zero_value__expect_exception(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)

        with self.assertRaises(Exception) as context:
            car.refuel(0)

        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test__drive__with_small_valid_distance__expect_fuel_amount_to_decrease(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)
        car.refuel(35)
        car.drive(100)

        expected = 35 - ((100 / 100) * self.valid_fuel_consumption)
        actual = car.fuel_amount

        self.assertEqual(expected, actual)

    def test__drive__with_big_invalid_distance__expect_exception(self):
        car = Car(self.valid_make, self.valid_model, self.valid_fuel_consumption, self.valid_fuel_capacity)

        with self.assertRaises(Exception) as context:
            car.drive(100)

        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")


if __name__ == '__main__':
    unittest.main()
