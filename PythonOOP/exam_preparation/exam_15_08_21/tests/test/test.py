from exam_preparation.exam_15_08_21.tests.pet_shop import PetShop
import unittest


class PetShopTests(unittest.TestCase):
    def test__init__with_valid_name__expect_correct_variables(self):
        shop = PetShop("pets")

        self.assertEqual(shop.name, "pets")
        self.assertEqual(shop.food, {})
        self.assertEqual(shop.pets, [])

    def test__add_food__with_valid_quantity_and_non_existing_name__should_add_food_with_given_quantity(self):
        shop = PetShop("pets")
        message = shop.add_food("food", 20)

        self.assertEqual(message, "Successfully added 20.00 grams of food.")
        self.assertEqual(shop.food, {"food": 20})

    def test__add_food__with_valid_quantity_and_existing_name__should_add_food_with_given_quantity(self):
        shop = PetShop("pets")
        shop.add_food("food", 20)

        message = shop.add_food("new_food", 30)

        self.assertEqual(message, "Successfully added 30.00 grams of new_food.")
        self.assertEqual(shop.food, {"food": 20, "new_food": 30})

    def test__add_food__with_negative_quantity__expect_exception(self):
        shop = PetShop("pets")

        with self.assertRaises(ValueError) as context:
            shop.add_food("food", -20)

        self.assertEqual(str(context.exception), 'Quantity cannot be equal to or less than 0')

    def test__add_food__with_zero_quantity__expect_exception(self):
        shop = PetShop("pets")

        with self.assertRaises(ValueError) as context:
            shop.add_food("food", 0)

        self.assertEqual(str(context.exception), 'Quantity cannot be equal to or less than 0')

    def test__add_pet__with_non_existing_name__should_add_pet(self):
        shop = PetShop("pets")
        message = shop.add_pet("Pet")

        self.assertEqual(message, "Successfully added Pet.")
        self.assertEqual(shop.pets, ["Pet"])

    def test__add_pet__with_existing_name__expect_exception(self):
        shop = PetShop("pets")
        shop.add_pet("Pet")

        with self.assertRaises(Exception) as context:
            shop.add_pet("Pet")

        self.assertEqual(str(context.exception), "Cannot add a pet with the same name")

    def test__feed_pet__with_non_existing_pet_name__expect_exception(self):
        shop = PetShop("pets")

        with self.assertRaises(Exception) as context:
            shop.feed_pet("food", "pet")

        self.assertEqual(str(context.exception), "Please insert a valid pet name")

    def test__feed_pet__with_existing_pet_and_non_existing_food__should_return_appropriate_message(self):
        shop = PetShop("pets")
        shop.add_pet("pet")

        message = shop.feed_pet("food", "pet")

        self.assertEqual(message, 'You do not have food')

    def test__feed_pet__with_existing_pet_and_little_food__should_add_1000gr_food(self):
        shop = PetShop("pet")
        shop.add_pet("cat")
        shop.add_food("food", 50)

        message = shop.feed_pet("food", "cat")
        self.assertEqual(message, "Adding food...")
        self.assertEqual(shop.food["food"], 1050)

    def test__feed_pet__with_valid_values__should_feed_given_pet(self):
        shop = PetShop("pet")
        shop.add_pet("cat")
        shop.add_food("food", 200)

        message = shop.feed_pet("food", "cat")

        self.assertEqual(message, "cat was successfully fed")
        self.assertEqual(shop.food["food"], 100)

    def test__repr__expect_correct_message(self):
        shop = PetShop("pets")
        shop.add_pet("cat")
        shop.add_pet("dog")
        shop.add_pet("bird")

        message = repr(shop)

        self.assertEqual(message, 'Shop pets:\nPets: cat, dog, bird')


if __name__ == '__main__':
    unittest.main()
