n = int(input())
players = {}

for _ in range(n):
    player, hp, mp = input().split()
    hp = int(hp)
    mp = int(mp)
    players[player] = {}
    players[player]['hp'] = hp
    players[player]['mp'] = mp

command = input()

while not command == 'End':
    if 'CastSpell' in command:
        action, name, mp_needed, spell_name = command.split(' - ')
        mp_needed = int(mp_needed)
        if mp_needed > players[name]['mp']:
            print(f"{name} does not have enough MP to cast {spell_name}!")
        else:
            players[name]['mp'] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {players[name]['mp']} MP!")
    elif 'TakeDamage' in command:
        action, name, damage, attacker = command.split(' - ')
        damage = int(damage)
        players[name]['hp'] -= damage
        if players[name]['hp'] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {players[name]['hp']} HP left!")
        else:
            players.pop(name)
            print(f"{name} has been killed by {attacker}!")
    elif 'Recharge' in command:
        action, name, amount = command.split(' - ')
        amount = int(amount)
        needed_mp = 200 - players[name]['mp']
        if amount < needed_mp:
            players[name]['mp'] += amount
            print(f"{name} recharged for {amount} MP!")
        else:
            players[name]['mp'] = 200
            print(f"{name} recharged for {needed_mp} MP!")
    elif 'Heal' in command:
        action, name, amount = command.split(' - ')
        amount = int(amount)
        needed_hp = 100 - players[name]['hp']
        if amount < needed_hp:
            players[name]['hp'] += amount
            print(f"{name} healed for {amount} HP!")
        else:
            players[name]['hp'] = 100
            print(f'{name} healed for {needed_hp} HP!')
    command = input()


sorted_players=dict(sorted(players.items(), key=lambda x:(-x[1]['hp'], x[0])))

for name in sorted_players:
    print(name)
    print(f'  HP: {players[name]["hp"]}')
    print(f'  MP: {players[name]["mp"]}')