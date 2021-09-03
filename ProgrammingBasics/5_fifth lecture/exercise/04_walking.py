goal=10000
command=input()
steps=0

while command!='Going home':
    steps+=int(command)
    if steps>=goal:
        print('Goal reached! Good job!')
        steps_over_the_goal=steps-goal
        print(f'{steps_over_the_goal} steps over the goal!')
        break

    command=input()

if steps<goal:
    home_steps=int(input())
    steps+=home_steps
    if steps>=goal:
        steps_over=steps-goal
        print('Goal reached! Good job!')
        print(f'{steps_over} steps over the goal!')
    else:
        needed=goal-steps
        print(f'{needed} more steps to reach goal.')