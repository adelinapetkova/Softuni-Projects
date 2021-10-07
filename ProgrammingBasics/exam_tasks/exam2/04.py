price_per_kg=12.45
number_of_cats=int(input())
small_cats=0
big_cats=0
giant_cats=0
total_grams=0

for i in range(number_of_cats):
    food_in_grams_per_cat=float(input())
    total_grams+=food_in_grams_per_cat
    if 100<=food_in_grams_per_cat<200:
        small_cats+=1
    elif 200<=food_in_grams_per_cat<300:
        big_cats+=1
    elif 300<=food_in_grams_per_cat<400:
        giant_cats+=1

total_kg=total_grams/1000
price_per_day=total_kg*price_per_kg

print(f'Group 1: {small_cats} cats.')
print(f'Group 2: {big_cats} cats.')
print(f'Group 3: {giant_cats} cats.')
print(f'Price for food per day: {price_per_day:.2f} lv.')
