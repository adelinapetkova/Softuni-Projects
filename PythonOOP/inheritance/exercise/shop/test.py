from inheritance.exercise.shop.food import Food
from inheritance.exercise.shop.drink import Drink
from inheritance.exercise.shop.product_repository import ProductRepository


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)