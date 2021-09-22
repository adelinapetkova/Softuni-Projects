name_of_tournament=input()
wins=0
loses=0
total_matches=0

while name_of_tournament!="End of tournaments":
    matches=int(input())
    total_matches+=matches
    for i in range(1,matches+1):
        our_team_points=int(input())
        opponent_points=int(input())
        if our_team_points>opponent_points:
            print(f'Game {i} of tournament {name_of_tournament}: win with {our_team_points-opponent_points} points.')
            wins+=1
        else:
            print(f'Game {i} of tournament {name_of_tournament}: lost with {opponent_points-our_team_points} points.')
            loses+=1
    name_of_tournament=input()

percentage_wins=(wins/total_matches)*100
percentage_loses=(loses/total_matches)*100

print(f'{percentage_wins:.2f}% matches win')
print(f'{percentage_loses:.2f}% matches lost')