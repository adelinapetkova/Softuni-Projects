import unittest

from testing.exercise.student.project.student import Student


class StudentTests(unittest.TestCase):
    def test__init__with_valid_values__expect_correct_variables(self):
        student = Student("student", {"basics": ["1"], "fundamentals": ["2"]})

        self.assertEqual(student.name, "student")
        self.assertEqual(student.courses, {"basics": ["1"], "fundamentals": ["2"]})

    def test__init__with_courses_equal_to_none__expect_correct_variables(self):
        student = Student("student")

        self.assertEqual(student.name, "student")
        self.assertEqual(student.courses, {})

    def test__enroll__with_existing_course__expect_updated_notes(self):
        student = Student("student", {"basics": ["1"], "fundamentals": ["2"]})
        message = student.enroll("basics", ["new", "new1"])

        expected = ["1", "new", "new1"]
        actual = student.courses["basics"]

        self.assertEqual(expected, actual)
        self.assertEqual(message, "Course already added. Notes have been updated.")

    def test__enroll__with_not_existing_course_and_without_last_argument_add_course_notes__expect_added_course_and_notes(
            self):
        student = Student("student", {"basics": ["1"], "fundamentals": ["2"]})
        message = student.enroll("advanced", ["adv", "python"])

        expected_courses = {"basics": ["1"], "fundamentals": ["2"], "advanced": ["adv", "python"]}
        actual_courses = student.courses

        self.assertEqual(expected_courses, actual_courses)
        self.assertEqual(message, "Course and course notes have been added.")

    def test__enroll__with_not_existing_course_and_with_last_argument_add_course_notes__expect_added_course_and_notes(
            self):
        student = Student("student", {"basics": ["1"], "fundamentals": ["2"]})
        message = student.enroll("advanced", ["adv", "python"], "Y")

        expected_courses = {"basics": ["1"], "fundamentals": ["2"], "advanced": ["adv", "python"]}
        actual_courses = student.courses

        self.assertEqual(expected_courses, actual_courses)
        self.assertEqual(message, "Course and course notes have been added.")

    def test__enroll__with_not_existing_course_and_with_last_argument_add_course_notes_equal_to_No__expect_added_course_and_notes(
            self):
        student = Student("student", {"basics": ["1"], "fundamentals": ["2"]})
        message = student.enroll("advanced", ["adv", "python"], "No")

        expected_courses = {"basics": ["1"], "fundamentals": ["2"], "advanced": []}
        actual_courses = student.courses

        self.assertEqual(expected_courses, actual_courses)
        self.assertEqual(message, "Course has been added.")

    def test__add_notes__with_existing_course_and_valid_notes__expect_notes_to_be_added(self):
        student = Student("student", {"basics": ["1"], "fundamentals": ["2"]})
        message = student.add_notes("basics", "basics_note")

        expected_notes = ["1", "basics_note"]
        actual_notes = student.courses["basics"]

        self.assertEqual(expected_notes, actual_notes)
        self.assertEqual(message, "Notes have been updated")

    def test__add_notes__with_non_existing_course__expect_exception(self):
        student = Student("student", {"basics": ["1"], "fundamentals": ["2"]})

        with self.assertRaises(Exception) as context:
            student.add_notes("advanced", "adv_note")

        self.assertEqual(str(context.exception), "Cannot add notes. Course not found.")

    def test__leave_course__with_existing_course__should_remove_course_from_dictionary(self):
        student = Student("student", {"basics": ["1"], "fundamentals": ["2"]})
        message = student.leave_course("basics")

        expected_courses = {"fundamentals": ["2"]}
        actual_courses = student.courses

        self.assertEqual(expected_courses, actual_courses)
        self.assertEqual(message, "Course has been removed")

    def test__leave_course__with_non_existing_course__expect_exception(self):
        student = Student("student", {"basics": ["1"], "fundamentals": ["2"]})

        with self.assertRaises(Exception) as context:
            student.leave_course("advanced")

        self.assertEqual(str(context.exception), "Cannot remove course. Course not found.")


if __name__ == '__main__':
    unittest.main()
