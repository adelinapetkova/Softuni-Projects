volume=int(input())
p1=int(input())
p2=int(input())
absent_hours=float(input())

liters_from_p1=p1*absent_hours
liters_from_p2=p2*absent_hours
liters_in_pool=liters_from_p2+liters_from_p1

if liters_in_pool<=volume:
    fullness_percentage=(liters_in_pool/volume)*100
    p1_percentage=(liters_from_p1/liters_in_pool)*100
    p2_percentage=(liters_from_p2/liters_in_pool)*100
    print(f'The pool is {fullness_percentage:.2f}% full. Pipe 1: {p1_percentage:.2f}%. Pipe 2: {p2_percentage:.2f}%.')
else:
    liters_in_excess=liters_in_pool-volume
    print(f'For {absent_hours:.2f} hours the pool overflows with {liters_in_excess:.2f} liters.')