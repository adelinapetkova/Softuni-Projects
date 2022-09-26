import unittest
from exam_preparation.exam_15_08_21.project import Train


class Tests(unittest.TestCase):
    def test__attributes__expect_correct_values(self):
        train = Train("train", 100)

        self.assertEqual(train.TRAIN_FULL, "Train is full")
        self.assertEqual(train.PASSENGER_EXISTS, "Passenger {} Exists")
        self.assertEqual(train.PASSENGER_NOT_FOUND, "Passenger Not Found")
        self.assertEqual(train.PASSENGER_ADD, "Added passenger {}")
        self.assertEqual(train.PASSENGER_REMOVED, "Removed {}")
        self.assertEqual(train.ZERO_CAPACITY, 0)

    def test__init__with_valid_values__expect_correct_variables(self):
        train = Train("name", 100)

        self.assertEqual(train.name, "name")
        self.assertEqual(train.capacity, 100)
        self.assertEqual(train.passengers, [])

    def test__add__with_enough_space_and_non_existing_name__should_add_passenger_to_list(self):
        train = Train("name", 10)
        message = train.add("person")

        self.assertEqual(message, "Added passenger person")
        self.assertEqual(train.passengers, ["person"])

    def test__add__with_not_enough_space_and_non_existing_name__expect_exception(self):
        train = Train("name", 1)
        train.add("person")

        with self.assertRaises(ValueError) as context:
            train.add("second person")

        self.assertEqual(str(context.exception), "Train is full")

    def test__add__with_enough_space_and_existing_name__expect_exception(self):
        train = Train("name", 10)
        train.add("person")

        with self.assertRaises(ValueError) as context:
            train.add("person")

        self.assertEqual(str(context.exception), "Passenger person Exists")

    def test__remove__with_existing_name__should_remove_passenger(self):
        train = Train("name", 10)
        train.add("person")

        message = train.remove("person")

        self.assertEqual(message, "Removed person")
        self.assertEqual(train.passengers, [])

    def test__remove__with_non_existing_name__expect_exception(self):
        train = Train("name", 10)
        train.add("person")

        with self.assertRaises(ValueError) as context:
            train.remove("non_existing")

        self.assertEqual(str(context.exception), "Passenger Not Found")


if __name__ == '__main__':
    unittest.main()
