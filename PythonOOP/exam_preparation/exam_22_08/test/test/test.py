from exam_preparation.exam_22_08.test.student_report_card import StudentReportCard
import unittest


class StudentReportCardTests(unittest.TestCase):
    def test__init__with_valid_values__expect_correct_variables(self):
        report_card = StudentReportCard("name", 4)

        self.assertEqual(report_card.student_name, "name")
        self.assertEqual(report_card.school_year, 4)
        self.assertEqual(report_card.grades_by_subject, {})

    def test__student_name_property__expect_correct_name(self):
        card = StudentReportCard("name", 4)

        self.assertEqual(card.student_name, "name")

    def test__student_name_setter__with_valid_value__expect_new_name(self):
        card = StudentReportCard("name", 4)
        card.student_name = "new"

        self.assertEqual(card.student_name, "new")

    def test__student_name_setter__with_invalid_value__expect_exception(self):
        card = StudentReportCard("name", 4)

        with self.assertRaises(ValueError) as context:
            card.student_name = ""

        self.assertEqual(str(context.exception), "Student Name cannot be an empty string!")

    def test__school_year_property__expect_correct_year(self):
        card = StudentReportCard("name", 4)

        self.assertEqual(card.school_year, 4)

    def test__school_year_setter__with_valid_values__expect_new_year(self):
        card = StudentReportCard("name", 4)
        card.school_year = 3

        self.assertEqual(card.school_year, 3)

    def test__school_year_setter__with_edge_valid_value__expect_new_year(self):
        card = StudentReportCard("name", 4)
        card.school_year = 1

        self.assertEqual(card.school_year, 1)

    def test__school_year_setter__with_edge_big_valid_value__expect_new_year(self):
        card = StudentReportCard("name", 4)
        card.school_year = 12

        self.assertEqual(card.school_year, 12)

    def test__school_year_setter__with_zero__expect_exception(self):
        card = StudentReportCard("name", 4)

        with self.assertRaises(ValueError) as context:
            card.school_year = 0

        self.assertEqual(str(context.exception), "School Year must be between 1 and 12!")

    def test__school_year_setter__with_big_value__expect_exception(self):
        card = StudentReportCard("name", 4)

        with self.assertRaises(ValueError) as context:
            card.school_year = 13

        self.assertEqual(str(context.exception), "School Year must be between 1 and 12!")

    def test__add_grade__with_existing_subject__should_add_grade_to_list(self):
        card = StudentReportCard("name", 4)
        card.grades_by_subject = {"maths": [4.50]}
        card.add_grade("maths", 5.00)

        self.assertEqual(card.grades_by_subject, {"maths": [4.50, 5.00]})

    def test__add_grade__with_non_existing_subject__should_add_grade_to_list(self):
        card = StudentReportCard("name", 4)
        card.add_grade("maths", 5.00)

        self.assertEqual(card.grades_by_subject, {"maths": [5.00]})

    def test__average_grade_by_subject__expect_correct_output(self):
        card = StudentReportCard("name", 4)
        card.grades_by_subject = {"math": [5.00, 6.00, 4.00], "literature": [4.00, 5.00]}

        self.assertEqual(card.average_grade_by_subject(), f"math: 5.00\nliterature: 4.50")

    def test__average_grade_for_all_subjects__expect_correct_average(self):
        card = StudentReportCard("name", 4)
        card.grades_by_subject = {"math": [5.00, 6.00, 4.00], "literature": [4.00, 5.00]}

        self.assertEqual(card.average_grade_for_all_subjects(), f"Average Grade: 4.80")

    def test__repr__expect_correct_report(self):
        card = StudentReportCard("name", 4)
        card.grades_by_subject = {"math": [5.00, 6.00, 4.00], "literature": [4.00, 5.00]}

        expected = f"Name: name\n" \
                   f"Year: 4\n" \
                   f"----------\n" \
                   f"math: 5.00\nliterature: 4.50\n" \
                   f"----------\n" \
                   f"Average Grade: 4.80"

        self.assertEqual(card.__repr__(), expected)
