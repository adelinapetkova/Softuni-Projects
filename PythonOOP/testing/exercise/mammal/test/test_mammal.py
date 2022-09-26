from testing.exercise.mammal.project.mammal import Mammal

import unittest


class MammalTests(unittest.TestCase):
    valid_name = "animal"
    valid_type = "cat"
    valid_sound = "meow"

    def test__init__with_valid_values__expect_correct_values(self):
        mammal = Mammal(self.valid_name, self.valid_type, self.valid_sound)

        self.assertEqual(self.valid_name, mammal.name)
        self.assertEqual(self.valid_sound, mammal.sound)
        self.assertEqual(self.valid_type, mammal.type)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test__make_sound__with_valid_values__expect_appropriate_message(self):
        mammal = Mammal(self.valid_name, self.valid_type, self.valid_sound)

        expected = f"{self.valid_name} makes {self.valid_sound}"
        actual = mammal.make_sound()

        self.assertEqual(expected, actual)

    def test__get_kingdom__expect_correct_kingdom(self):
        mammal = Mammal(self.valid_name, self.valid_type, self.valid_sound)

        expected = "animals"
        actual = mammal.get_kingdom()

        self.assertEqual(expected, actual)

    def test__info__expect_correct_message(self):
        mammal = Mammal(self.valid_name, self.valid_type, self.valid_sound)

        expected = f"{self.valid_name} is of type {self.valid_type}"
        actual = mammal.info()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
