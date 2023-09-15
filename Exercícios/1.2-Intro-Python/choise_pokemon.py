import json
import random

def shot(pokemon_name):
    num_of_shots = 0
    max_shots = len(pokemon_name)
    
    print("Bem-vindo ao jogo de adivinhação do Pokémon!")
    
    while num_of_shots < max_shots:
        num_of_shots += 1
        user_guess = input(f"Tentativa {num_of_shots}: Quem é esse Pokémon? ")
        
        if user_guess == pokemon_name[:num_of_shots]:
            print("Você acertou a parte", num_of_shots, "do nome!")
        else:
            print("Dica: ", end="")
            for i in range(num_of_shots):
                print(pokemon_name[i], end="")
            print(" (Até agora)")
            print("Você errou! Tente novamente.")
    
    print("Parabéns, você acertou o nome completo! É", pokemon_name)

if __name__ == "__main__":
    with open("pokemons.json") as file:
        pokemons = json.load(file)["results"]
        pokemon = random.choice(pokemons)
        pokemon_name = pokemon["name"]

    shot(pokemon_name)
