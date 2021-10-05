pages=899
covers=2
price_per_page=float(input())
price_per_cover=float(input())
percentage_discount=int(input())
price_for_design=float(input())
percentage_paid_by_the_team=int(input())

total=pages*price_per_page+covers*price_per_cover
total_with_discount=total-(total*percentage_discount/100)
final=total_with_discount+price_for_design

avtonom_paying=final-(final*percentage_paid_by_the_team/100)

print(f'Avtonom should pay {avtonom_paying:.2f} BGN.')