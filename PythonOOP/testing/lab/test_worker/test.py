from worker import Worker
import unittest


class WorkerTests(unittest.TestCase):
    def test_init__with_valid_name_salary_energy__expect_correct_value(self):
        valid_name="Andy"
        valid_salary=2000
        valid_energy=20

        worker=Worker(valid_name, valid_salary, valid_energy)

        self.assertEqual(valid_name, worker.name)
        self.assertEqual(valid_salary, worker.salary)
        self.assertEqual(valid_energy, worker.energy)

    def test_rest__with_valid_energy__expect_energy_increase(self):
        valid_name = "Andy"
        valid_salary = 2000
        valid_energy = 20

        worker = Worker(valid_name, valid_salary, valid_energy)

        worker.rest()

        self.assertEqual(valid_energy+1, worker.energy)

    def test__work__with_energy_0__expect_exception(self):
        valid_name = "Andy"
        valid_salary = 2000
        valid_energy = 0

        worker = Worker(valid_name, valid_salary, valid_energy)

        with self.assertRaises(Exception) as context:
            worker.work()

        self.assertEqual(str(context.exception), "Not enough energy.")

    def test__work__with_negative_energy__expect_exception(self):
        valid_name = "Andy"
        valid_salary = 2000
        valid_energy = -1

        worker = Worker(valid_name, valid_salary, valid_energy)

        with self.assertRaises(Exception) as context:
            worker.work()

        self.assertEqual(str(context.exception), "Not enough energy.")

    def test__work__with_valid_values__expect_salary_increase(self):
        valid_name = "Andy"
        valid_salary = 2000
        valid_energy = 20

        worker = Worker(valid_name, valid_salary, valid_energy)

        worker.work()
        worker.work()

        self.assertEqual(worker.money, 2*valid_salary)

    def test__work__with_valid_values__expect_energy_decrease(self):
        valid_name = "Andy"
        valid_salary = 2000
        valid_energy = 20

        worker = Worker(valid_name, valid_salary, valid_energy)

        worker.work()

        self.assertEqual(worker.energy, valid_energy-1)

    def test__get_info__with_valid_values__expect_proper_string(self):
        valid_name = "Andy"
        valid_salary = 2000
        valid_energy = 20

        worker = Worker(valid_name, valid_salary, valid_energy)
        actual_string=worker.get_info()
        expected_string=f'{valid_name} has saved {worker.money} money.'

        self.assertEqual(actual_string, expected_string)


if __name__ == '__main__':
    unittest.main()
