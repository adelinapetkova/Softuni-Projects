from first_steps.exercise.first_steps_project.pokemon import Pokemon


class Trainer():
    def __init__(self, name: str):
        self.pokemons = []
        self.name = name

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f'Caught {pokemon.name} with health {pokemon.health}'
        else:
            return 'This pokemon is already caught'

    def release_pokemon(self, pokemon_name: str):
        is_pokemon_in_list = False
        pokemon_to_remove = None
        for p in self.pokemons:
            if p.name == pokemon_name:
                is_pokemon_in_list = True
                pokemon_to_remove = p
                break
        if is_pokemon_in_list:
            self.pokemons.remove(pokemon_to_remove)
            return f'You have released {pokemon_name}'
        else:
            return 'Pokemon is not caught'

    def trainer_data(self):
        output = [f'Pokemon Trainer {self.name}', f'Pokemon count {len(self.pokemons)}']

        for p in self.pokemons:
            output.append(f'- {p.name} with health {p.health}')

        return '\n'.join(output)




