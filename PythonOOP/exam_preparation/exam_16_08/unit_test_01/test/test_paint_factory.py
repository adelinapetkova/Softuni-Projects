import unittest
from exam_preparation.exam_16_08.unit_test_01.project.factory.paint_factory import PaintFactory


class PaintFactoryTests(unittest.TestCase):

    def test__init__with_valid_values__expect_correct_variables(self):
        paint_factory = PaintFactory("factory", 200)

        self.assertEqual(paint_factory.name, "factory")
        self.assertEqual(paint_factory.capacity, 200)

    def test__add_ingredient__with_valid_type_able_to_add_and_type_not_in_ingredients__expect_type_added_to_ingredients_with_given_quantity(
            self):
        paint_factory = PaintFactory("factory", 200)
        paint_factory.add_ingredient("white", 100)

        self.assertEqual(paint_factory.ingredients, {"white": 100})

    def test__add_ingredient__with_valid_type_and_edge_can_add_and_type_not_in_ingredients__expect_type_added_to_ingredients_with_given_quantity(
            self):
        paint_factory = PaintFactory("factory", 200)
        paint_factory.add_ingredient("white", 200)

        self.assertEqual(paint_factory.ingredients, {"white": 200})

    def test__add_ingredient__with_valid_type_able_to_add_and_type_in_ingredients__expect_given_quantity_added_to_type(
            self):
        paint_factory = PaintFactory("factory", 200)
        paint_factory.add_ingredient("white", 100)
        paint_factory.add_ingredient("white", 50)

        self.assertEqual(paint_factory.ingredients, {"white": 150})

    def test__add_ingredient__with_valid_type_and_unable_to_add__expect_exception(self):
        paint_factory = PaintFactory("factory", 200)

        with self.assertRaises(ValueError) as context:
            paint_factory.add_ingredient("white", 300)

        self.assertEqual(str(context.exception), "Not enough space in factory")

    def test__add_ingredient__with_invalid_type__expect_exception(self):
        paint_factory = PaintFactory("factory", 200)

        with self.assertRaises(TypeError) as context:
            paint_factory.add_ingredient("purple", 100)

        self.assertEqual(str(context.exception), "Ingredient of type purple not allowed in PaintFactory")

    def test__remove_ingredient__with_existing_type_and_quantity_less_than_total_quantity_for_product__expect_decreasing_product_quantity(
            self):
        paint_factory = PaintFactory("factory", 200)
        paint_factory.add_ingredient("white", 100)
        paint_factory.remove_ingredient("white", 50)

        self.assertEqual(paint_factory.ingredients["white"], 50)

    def test__remove_ingredient__with_existing_type_and_quantity_equal_to_total_quantity_for_product__expect_decreasing_product_quantity(
            self):
        paint_factory = PaintFactory("factory", 200)
        paint_factory.add_ingredient("white", 100)
        paint_factory.remove_ingredient("white", 100)

        self.assertEqual(paint_factory.ingredients["white"], 0)

    def test__remove_ingredient__with_existing_type_and_quantity_more_than_total_quantity_for_product__expect_exception(
            self):
        paint_factory = PaintFactory("factory", 200)
        paint_factory.add_ingredient("white", 100)

        with self.assertRaises(ValueError) as context:
            paint_factory.remove_ingredient("white", 150)

        self.assertEqual(str(context.exception), "Ingredients quantity cannot be less than zero")

    def test__remove_ingredient__with_non_existing_type__expect_exception(self):
        paint_factory = PaintFactory("factory", 200)
        paint_factory.add_ingredient("white", 100)

        with self.assertRaises(KeyError) as context:
            paint_factory.remove_ingredient("yellow", 150)

        self.assertIn("No such ingredient in the factory", str(context.exception))

    def test__products_property__should_return_ingredients_dictionary(self):
        paint_factory = PaintFactory("factory", 200)
        paint_factory.add_ingredient("white", 100)

        self.assertEqual(paint_factory.products, {"white": 100})
