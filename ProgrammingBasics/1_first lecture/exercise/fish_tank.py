length_in_cm=int(input())
width_in_cm=int(input())
height_in_cm=int(input())
percentage_occupied_volume=float(input())

volume_in_cm=width_in_cm*length_in_cm*height_in_cm

volume_in_dm=volume_in_cm/1000

liters_water=volume_in_dm - (percentage_occupied_volume*volume_in_dm)/100

print(liters_water)