worker_1=int(input())
worker_2=int(input())
worker_3=int(input())

number_of_clients=int(input())

served_clients_per_hour=worker_1+worker_2+worker_3
hours=0

while number_of_clients>0:
    hours+=1
    if hours%4==0:
        continue
    number_of_clients-=served_clients_per_hour

print(f'Time needed: {hours}h.')
