visitors=int(input())

back_count=0
chest_count=0
legs_count=0
abs_count=0
protein_shakes=0
protein_bars=0

for i in range(visitors):
    activity=input()
    if activity=='Back':
        back_count+=1
    elif activity=='Chest':
        chest_count+=1
    elif activity=='Legs':
        legs_count+=1
    elif activity=='Abs':
        abs_count+=1
    elif activity=='Protein shake':
        protein_shakes+=1
    elif activity=='Protein bar':
        protein_bars+=1

percentage_people_working_out=((back_count+chest_count+legs_count+abs_count)/visitors)*100
percentage_people_for_protein=((protein_shakes+protein_bars)/visitors)*100

print(f'{back_count} - back')
print(f'{chest_count} - chest')
print(f'{legs_count} - legs')
print(f'{abs_count} - abs')
print(f'{protein_shakes} - protein shake')
print(f'{protein_bars} - protein bar')
print(f'{percentage_people_working_out:.2f}% - work out')
print(f'{percentage_people_for_protein:.2f}% - protein')



