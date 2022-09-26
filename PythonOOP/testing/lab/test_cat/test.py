from cat import Cat

import unittest


class CatTests(unittest.TestCase):
    def test__eat__with_valid_values__expect_size_increase(self):
        valid_name="Tom"

        cat=Cat(valid_name)
        valid_size=cat.size

        cat.eat()
        actual_size=cat.size
        expected_size=valid_size+1

        self.assertEqual(actual_size, expected_size)

    def test__eat__with_valid_values__expect_cat_to_be_fed(self):
        valid_name="Tom"
        cat=Cat(valid_name)

        cat.eat()

        self.assertEqual(cat.fed, True)

    def test__eat__with_fed_cat__expect_exception(self):
        valid_name = "Tom"
        cat = Cat(valid_name)

        cat.eat()

        with self.assertRaises(Exception) as context:
            cat.eat()

        self.assertEqual(str(context.exception), "Already fed.")

    def test__sleep__with_hungry_cat__expect_exception(self):
        valid_name = "Tom"
        cat = Cat(valid_name)

        with self.assertRaises(Exception) as context:
            cat.sleep()

        self.assertEqual(str(context.exception), "Cannot sleep while hungry")

    def test__sleep__with_cat_that_slept__expect_cat_not_sleepy(self):
        valid_name = "Tom"
        cat = Cat(valid_name)

        cat.eat()
        cat.sleep()

        self.assertEqual(cat.sleepy, False)


if __name__ == '__main__':
    unittest.main()