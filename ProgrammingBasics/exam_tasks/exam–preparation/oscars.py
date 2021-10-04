actor=input()
points_from_the_academy=float(input())
n=int(input())
total_points = points_from_the_academy

for i in range(n):
    jury=input()
    points_from_jury=float(input())
    points=len(jury)*points_from_jury/2
    total_points+=points
    if total_points>1250.5:
        break

if total_points>1250.5:
    print(f'Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!')
else:
    needed=1250.5-total_points
    print(f'Sorry, {actor} you need {needed:.1f} more!')