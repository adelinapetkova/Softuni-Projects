import unittest

from testing.exercise.hero.project.hero import Hero


class HeroTests(unittest.TestCase):
    username = "hero"
    level = 20
    health = 45.5
    damage = 5.5

    def test__init__with_valid_values__expect_correct_values_to_variables(self):
        hero = Hero(self.username, self.level, self.health, self.damage)

        self.assertEqual(self.username, hero.username)
        self.assertEqual(self.level, hero.level)
        self.assertEqual(self.health, hero.health)
        self.assertEqual(self.damage, hero.damage)

    def test__battle__with_the_same_username_for_enemy__expect_exception(self):
        hero = Hero(self.username, self.level, self.health, self.damage)
        enemy = Hero(self.username, self.level, self.health, self.damage)

        with self.assertRaises(Exception) as context:
            hero.battle(enemy)

        self.assertEqual(str(context.exception), "You cannot fight yourself")

    def test_battle__with_negative_hero_health__expect_exception(self):
        hero = Hero(self.username, self.level, -20.5, self.damage)
        enemy = Hero("enemy", self.level, self.health, self.damage)

        with self.assertRaises(Exception) as context:
            hero.battle(enemy)

        self.assertEqual(str(context.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle__with_zero_hero_health__expect_exception(self):
        hero = Hero(self.username, self.level, 0, self.damage)
        enemy = Hero("enemy", self.level, self.health, self.damage)

        with self.assertRaises(Exception) as context:
            hero.battle(enemy)

        self.assertEqual(str(context.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle__with_negative_enemy_health__expect_exception(self):
        hero = Hero(self.username, self.level, self.health, self.damage)
        enemy = Hero("enemy", self.level, -21.5, self.damage)

        with self.assertRaises(Exception) as context:
            hero.battle(enemy)

        self.assertEqual(str(context.exception), f"You cannot fight {enemy.username}. He needs to rest")

    def test_battle__with_zero_enemy_health__expect_exception(self):
        hero = Hero(self.username, self.level, self.health, self.damage)
        enemy = Hero("enemy", self.level, 0, self.damage)

        with self.assertRaises(Exception) as context:
            hero.battle(enemy)

        self.assertEqual(str(context.exception), f"You cannot fight {enemy.username}. He needs to rest")

    def test__battle__with_valid_values__expect_damage_and_health_changed(self):
        hero = Hero(self.username, 20, 40, 6)
        enemy = Hero("enemy", 20, 30, 6)
        hero.battle(enemy)

        expected_hero_damage = 6 * 20
        expected_enemy_damage = 6 * 20
        expected_hero_health = 40 - expected_enemy_damage
        expected_enemy_health = 30 - expected_hero_damage

        self.assertEqual(expected_enemy_health, enemy.health)
        self.assertEqual(expected_hero_health, hero.health)

    def test__battle__with_negative_healths_after_battle__expect_draw_message(self):
        hero = Hero("hero", 20, 20, 10)
        enemy = Hero("enemy", 25, 30, 15)
        message = hero.battle(enemy)

        self.assertEqual(message, "Draw")

    def test__battle__with_zero_healths_after_battle__expect_draw_message(self):
        hero = Hero("hero", 20, 300, 10)
        enemy = Hero("enemy", 20, 200, 15)
        message = hero.battle(enemy)

        self.assertEqual(message, "Draw")

    def test__battle__with_enemy_zero_health_after_battle__expect_win_message_and_increase_values_for_hero(self):
        hero = Hero("hero", 20, 400, 10)
        enemy = Hero("enemy", 20, 200, 15)
        message = hero.battle(enemy)

        self.assertEqual(21, hero.level)
        self.assertEqual(105, hero.health)
        self.assertEqual(15, hero.damage)
        self.assertEqual(message, "You win")

    def test__battle__with_enemy_negative_health_after_battle__expect_win_message_and_increase_values_for_hero(self):
        hero = Hero("hero", 20, 400, 10)
        enemy = Hero("enemy", 20, 100, 15)
        message = hero.battle(enemy)

        self.assertEqual(21, hero.level)
        self.assertEqual(105, hero.health)
        self.assertEqual(15, hero.damage)
        self.assertEqual(message, "You win")

    def test__battle__with_positive_healths_after_battle__expect_lose_message_and_increase_values_for_enemy(self):
        hero = Hero("hero", 20, 400, 10)
        enemy = Hero("enemy", 20, 300, 15)
        message = hero.battle(enemy)

        self.assertEqual(21, enemy.level)
        self.assertEqual(105, enemy.health)
        self.assertEqual(20, enemy.damage)
        self.assertEqual(message, "You lose")

    def test__str__expect_correct_message(self):
        hero = Hero("hero", 20, 400, 10)

        expected = f"Hero hero: 20 lvl\n" \
                   f"Health: 400\n" \
                   f"Damage: 10\n"
        actual = hero.__str__()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
