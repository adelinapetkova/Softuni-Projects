bought_food_in_kg=int(input())
grams_per_day=input()
total_grams=0

while grams_per_day!='Adopted':
    total_grams+=int(grams_per_day)
    grams_per_day=input()

bought_food_in_grams=bought_food_in_kg*1000

if bought_food_in_grams>=total_grams:
    left=bought_food_in_grams-total_grams
    print(f'Food is enough! Leftovers: {left} grams.')
else:
    needed=total_grams-bought_food_in_grams
    print(f'Food is not enough. You need {needed} grams more.')