from exam.testingexam.project.team import Team
import unittest


class TeamTests(unittest.TestCase):
    def test__init__with_valid_values__expect_correct_variables(self):
        team = Team("name")

        self.assertEqual(team.name, "name")
        self.assertEqual(team.members, {})

    def test__init__with_invalid_values__expect_exception(self):
        with self.assertRaises(ValueError) as context:
            team = Team("1ame")

        self.assertEqual(str(context.exception), "Team Name can contain only letters!")

    def test__add_member__with_non_existing_names__should_add_names_and_ages_to_members(self):
        team = Team("name")
        message = team.add_member(person1=23, person2=34, person3=45)

        self.assertEqual(team.members, {"person1": 23, "person2": 34, "person3": 45})
        self.assertEqual(message, "Successfully added: person1, person2, person3")

    def test__add_member__with_existing_names__should_not_add_existing_names_to_members(self):
        team = Team("name")
        team.add_member(person1=23, person2=34, person3=45)
        message = team.add_member(person1=34)

        self.assertEqual(team.members, {"person1": 23, "person2": 34, "person3": 45})
        self.assertEqual(message, "Successfully added: ")

    def test__remove_member__with_existing_name__should_remove_person_from_members(self):
        team = Team("name")
        team.add_member(person1=23, person2=34, person3=45)
        message = team.remove_member("person1")

        self.assertEqual(team.members, {"person2": 34, "person3": 45})
        self.assertEqual(message, "Member person1 removed")

    def test__remove_member__with_non_existing_name__should_return_correct_message(self):
        team = Team("name")
        team.add_member(person1=23, person2=34, person3=45)
        message = team.remove_member("person4")

        self.assertEqual(team.members, {"person1": 23, "person2": 34, "person3": 45})
        self.assertEqual(message, "Member with name person4 does not exist")

    def test__gt__with_bigger_team__expect_false(self):
        team1 = Team("small")
        team2 = Team("big")
        team1.add_member(person1=23)
        team2.add_member(person1=23, person2=34, person3=45)

        expected = False
        actual = team1 > team2

        self.assertEqual(expected, actual)

    def test__gt__with_smaller_team__expect_true(self):
        team1 = Team("big")
        team2 = Team("small")
        team1.add_member(person1=23, person2=34, person3=45)
        team2.add_member(person1=23)

        expected = True
        actual = team1 > team2

        self.assertEqual(expected, actual)

    def test__len__expect_correct_return(self):
        team = Team("name")
        team.add_member(person1=23, person2=34, person3=45)

        expected = 3
        actual = len(team)

        self.assertEqual(expected, actual)

    def test__add__expect_new_team(self):
        team1 = Team("one")
        team2 = Team("two")
        team1.add_member(person1=23, person2=34, person3=45)
        team2.add_member(person4=23)
        new_team = Team("onetwo")
        new_team.add_member(person1=23, person2=34, person3=45, person4=23)

        returned_new_team = team1 + team2
        self.assertEqual(returned_new_team.name, new_team.name)
        self.assertEqual(returned_new_team.members, new_team.members)

    def test__str__expect_correct_info(self):
        team = Team("name")
        team.add_member(person1=23, person2=34, person3=45)

        expected = "Team name: name\n" \
                   "Member: person3 - 45-years old\n" \
                   "Member: person2 - 34-years old\n" \
                   "Member: person1 - 23-years old"
        actual = str(team)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()