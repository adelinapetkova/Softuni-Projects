import unittest

from testing.exercise.vehicle.project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    valid_fuel = 12.5
    valid_horse_power = 150.5

    def test__init__with_valid_values__should_return_correct_values_for_variables(self):
        vehicle = Vehicle(self.valid_fuel, self.valid_horse_power)

        self.assertEqual(self.valid_fuel, vehicle.fuel)
        self.assertEqual(self.valid_horse_power, vehicle.horse_power)
        self.assertEqual(self.valid_fuel, vehicle.capacity)
        self.assertEqual(1.25, vehicle.fuel_consumption)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test__drive__with_needed_fuel_equal_to_fuel__expect_fuel_equal_to_zero(self):
        vehicle = Vehicle(self.valid_fuel, self.valid_horse_power)
        vehicle.drive(10)

        expected = 0
        actual = vehicle.fuel

        self.assertEqual(expected, actual)

    def test__drive__with_little_kilometers__expect_fuel_decrease(self):
        vehicle = Vehicle(self.valid_fuel, self.valid_horse_power)
        vehicle.drive(5)

        expected = self.valid_fuel - (1.25 * 5)
        actual = vehicle.fuel

        self.assertEqual(expected, actual)

    def test__drive__with_a_lot_of_km__should_return_exception(self):
        vehicle = Vehicle(self.valid_fuel, self.valid_horse_power)

        with self.assertRaises(Exception) as context:
            vehicle.drive(100)

        self.assertEqual(str(context.exception), "Not enough fuel")

    def test__refuel__with_valid_fuel__expect_fuel_to_increase(self):
        vehicle = Vehicle(self.valid_fuel, self.valid_horse_power)
        vehicle.drive(5)
        vehicle.refuel(4)

        expected = self.valid_fuel - (1.25 * 5) + 4
        actual = vehicle.fuel

        self.assertEqual(expected, actual)

    def test__refuel__with_too_much_fuel__expect_exception(self):
        vehicle = Vehicle(self.valid_fuel, self.valid_horse_power)

        with self.assertRaises(Exception) as context:
            vehicle.refuel(20)

        self.assertEqual(str(context.exception), "Too much fuel")

    def test__str__should_return_correct_message(self):
        vehicle = Vehicle(self.valid_fuel, self.valid_horse_power)

        expected = f"The vehicle has {self.valid_horse_power} " \
                   f"horse power with {self.valid_fuel} fuel left and 1.25 fuel consumption"
        actual = vehicle.__str__()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
