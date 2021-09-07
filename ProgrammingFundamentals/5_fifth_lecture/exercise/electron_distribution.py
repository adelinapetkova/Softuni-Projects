electrons=int(input())
shell_number=0
shells=[]

while electrons>0:
    shell_number+=1
    electrons_per_shell=2*(shell_number**2)
    if electrons>=electrons_per_shell:
        electrons-=electrons_per_shell
        shells.append(electrons_per_shell)
    else:
        shells.append(electrons)
        electrons-=electrons_per_shell

print(shells)