import math

days=int(input())
kg_food=int(input())
dog_food_per_day=float(input())
cat_food_per_day=float(input())
turtoise_food_per_day_in_grams=float(input())

dog_food=days*dog_food_per_day
cat_food=days*cat_food_per_day
turtoise_food=(turtoise_food_per_day_in_grams/1000)*days

total_kilograms=dog_food+cat_food+turtoise_food

if kg_food>=total_kilograms:
    left=math.floor(kg_food-total_kilograms)
    print(f'{left} kilos of food left.')
else:
    needed_food=math.ceil(total_kilograms-kg_food)
    print(f'{needed_food} more kilos of food are needed.')