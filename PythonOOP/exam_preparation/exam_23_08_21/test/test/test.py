from exam_preparation.exam_23_08_21.test.library import Library
import unittest


class LibraryTests(unittest.TestCase):
    def test__init__with_valid_name__expect_correct_values_for_variables(self):
        library = Library("lib")

        self.assertEqual(library.name, "lib")
        self.assertEqual(library.books_by_authors, {})
        self.assertEqual(library.readers, {})

    def test__init__with_invalid_name__expect_exception(self):
        with self.assertRaises(ValueError) as context:
            library = Library("")

        self.assertEqual(str(context.exception), "Name cannot be empty string!")

    def test__add_book__with_non_existing_author_and_title__should_add_values_to_books_by_authors(self):
        library = Library("lib")
        library.add_book("author", "title")

        self.assertEqual(library.books_by_authors, {"author": ["title"]})

    def test__add_book__with_existing_author_and_non_existing_title__should_add_title_to_authors_list(self):
        library = Library("lib")
        library.add_book("author", "title")
        library.add_book("author", "new_title")

        self.assertEqual(library.books_by_authors, {"author": ["title", "new_title"]})

    def test__add_book__with_existing_author_and_title__should_not_add_values_to_books_by_authors(self):
        library = Library("lib")
        library.add_book("author", "title")
        library.add_book("author", "title")

        self.assertEqual(library.books_by_authors, {"author": ["title"]})

    def test__add_reader__with_non_existing_reader__should_add_name_to_readers(self):
        library = Library("lib")
        library.add_reader("person")

        self.assertEqual(library.readers, {"person": []})

    def test__add_reader__with_existing_reader__expect_appropriate_message(self):
        library = Library("lib")
        library.add_reader("person")

        message = library.add_reader("person")
        self.assertEqual(message, "person is already registered in the lib library.")

    def test__rent_book__with__non_existing_reader_name__expect_correct_message(self):
        library = Library("lib")
        message = library.rent_book("name", "author", "title")

        self.assertEqual(message, "name is not registered in the lib Library.")

    def test__rent_book__with__non_existing_book_author__expect_correct_message(self):
        library = Library("lib")
        library.add_reader("name")
        message = library.rent_book("name", "author", "title")

        self.assertEqual(message, "lib Library does not have any author's books.")

    def test__rent_book__with__non_existing_book_title__expect_correct_message(self):
        library = Library("lib")
        library.add_reader("name")
        library.add_book("author", "existing_title")
        message = library.rent_book("name", "author", "title")

        self.assertEqual(message, """lib Library does not have author's "title".""")

    def test__rent_book__with__existing_values__expect_correct_changes(self):
        library = Library("lib")
        library.add_reader("name")
        library.add_book("author", "existing_title")
        library.rent_book("name", "author", "existing_title")

        self.assertEqual(library.readers, {"name": [{"author": "existing_title"}]})
        self.assertEqual(library.books_by_authors, {"author": []})


if __name__ == '__main__':
    unittest.main()
