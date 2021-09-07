teamA=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
teamB=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

cards=input().split()

for command in cards:
    splited_command=command.split('-')
    team=splited_command[0]
    player=splited_command[1]
    if team=='A' and int(player) in teamA:
        teamA.remove(int(player))
    elif team=='B' and int(player) in teamB:
        teamB.remove(int(player))
    if len(teamA)<7 or len(teamB)<7:
        print(f'Team A - {len(teamA)}; Team B - {len(teamB)}')
        print('Game was terminated')
        break


if len(teamA)>=7 and len(teamB)>=7:
   print(f'Team A - {len(teamA)}; Team B - {len(teamB)}')