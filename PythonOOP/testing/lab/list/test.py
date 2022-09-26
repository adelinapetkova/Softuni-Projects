from extended_list import IntegerList

import unittest


class IntegerListTests(unittest.TestCase):
    tuple_with_elements = (1, 2, '3', [2, 2, 3], "str", 2.3, 8, {1: "1"})
    integers_from_tuple = [x for x in tuple_with_elements if type(x) == int]

    def test__constructor__expect_list_of_ints(self):
        int_list = IntegerList(*self.tuple_with_elements)

        actual_return = int_list.get_data()
        expected_return = []+self.integers_from_tuple

        self.assertListEqual(expected_return, actual_return)

    def test__init__with_values_of_different_types__expect_int_list(self):
        IntegerList(*self.tuple_with_elements)

    def test__add__with_int_value__expect_list_of_ints(self):
        int_list = IntegerList(*self.tuple_with_elements)

        actual_data = int_list.add(25)
        expected_data = self.integers_from_tuple+[25]

        self.assertListEqual(actual_data, expected_data)

    def test__add__with_non_int_value__expect_exception(self):
        int_list = IntegerList(*self.tuple_with_elements)
        with self.assertRaises(ValueError) as context:
            int_list.add("2")

        self.assertEqual(str(context.exception), "Element is not Integer")

    def test__remove_index__with_valid_index__expect_list_without_element_on_that_index(self):
        int_list = IntegerList(*self.tuple_with_elements)

        actual_return = int_list.remove_index(2)
        expected_return = []+self.integers_from_tuple

        self.assertEqual(expected_return.pop(2), actual_return)
        self.assertListEqual(expected_return, int_list.get_data())

    def test__remove_index__with_big_index__expect__exception(self):
        int_list = IntegerList(*self.tuple_with_elements)
        with self.assertRaises(IndexError) as context:
            int_list.remove_index(10)

        self.assertEqual(str(context.exception), "Index is out of range")

    def test__remove_index__with_index_equal_to_length__expect__exception(self):
        int_list = IntegerList(*self.tuple_with_elements)
        with self.assertRaises(IndexError) as context:
            int_list.remove_index(len(int_list.get_data()))

        self.assertEqual(str(context.exception), "Index is out of range")

    def test__remove_index__with_small_index__expect__exception(self):
        int_list = IntegerList(*self.tuple_with_elements)
        with self.assertRaises(IndexError):
            int_list.remove_index(-10)

    def test__get__with_valid_index__expect_element_on_that_index(self):
        int_list = IntegerList(*self.tuple_with_elements)

        actual_return = int_list.get(2)
        expected_return = [x for x in self.tuple_with_elements if type(x) == int][2]

        self.assertEqual(expected_return, actual_return)

    def test__get__with_big_index__expect_exception(self):
        int_list = IntegerList(*self.tuple_with_elements)

        with self.assertRaises(IndexError) as context:
            int_list.get(10)

        self.assertEqual(str(context.exception), "Index is out of range")

    def test__get__with_index_equal_to_length__expect_exception(self):
        int_list = IntegerList(*self.tuple_with_elements)

        with self.assertRaises(IndexError) as context:
            int_list.get(len(int_list.get_data()))

        self.assertEqual(str(context.exception), "Index is out of range")

    def test__get__with_small_index__expect_exception(self):
        int_list = IntegerList(*self.tuple_with_elements)

        with self.assertRaises(IndexError):
            int_list.get(-10)

    def test__insert__with_valid_values__expect_correct_list(self):
        int_list = IntegerList(*self.tuple_with_elements)
        int_list.insert(2, 6)

        expected=[]+self.integers_from_tuple
        expected.insert(2, 6)

        self.assertEqual(expected, int_list.get_data())

    def test__insert__with_invalid_big_index_and_valid_element__expect_exception(self):
        int_list = IntegerList(*self.tuple_with_elements)

        with self.assertRaises(IndexError) as context:
            int_list.insert(10, 14)

        self.assertEqual(str(context.exception), "Index is out of range")

    def test__insert__with_invalid_index_equal_to_length_and_valid_element__expect_exception(self):
        int_list = IntegerList(*self.tuple_with_elements)

        with self.assertRaises(IndexError) as context:
            int_list.insert(len(int_list.get_data()), 14)

        self.assertEqual(str(context.exception), "Index is out of range")

    def test__insert__with_valid_index_and_invalid_element__expect__exception(self):
        int_list = IntegerList(*self.tuple_with_elements)

        with self.assertRaises(ValueError) as context:
            int_list.insert(1, "12")

        self.assertEqual(str(context.exception), "Element is not Integer")

    def test__get_biggest__expect_biggest_element(self):
        int_list = IntegerList(*self.tuple_with_elements)

        expected_return = sorted(self.integers_from_tuple, reverse=True)[0]
        actual_return = int_list.get_biggest()

        self.assertEqual(expected_return, actual_return)

    def test__get_index__expect_element_from_index(self):
        int_list = IntegerList(*self.tuple_with_elements)

        expected = self.integers_from_tuple.index(2)
        actual = int_list.get_index(2)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()