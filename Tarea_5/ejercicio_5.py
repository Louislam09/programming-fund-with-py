import requests
import json
from os import system

url = "https://pokeapi.co/api/v2/pokemon/"

title = """
------------------------------------------------
Programa que a acepta el nombre de un pokemonen 
ingles y Muestre al menos 2 habilidades o ataques
                de ese pokemon.
------------------------------------------------
"""


def got_pokemon():
    system('cls')
    print(title)

    pokemon_name = input("Escribe el nombre del pokemon(en ingles): ").lower()

    try:
        response = requests.get(url + pokemon_name, timeout=5)

        try:
            pokemon_name = response.json()
            pokemon_abilities = pokemon_name["abilities"]
            print(f"Este Pokemon posee {len(pokemon_abilities)} habilidad(es)")
            # print(pokemon_abilities)

            print('\n')
            for ability in range(len(pokemon_abilities)):
                print(f"Habilidad {ability+1}:")
                print(pokemon_abilities[ability]["ability"]["name"])
                print('\n')

        except json.JSONDecodeError:
            print(f"""\n
    ------------------------------------------------------
                    EL POKEMON NO EXISTE!
    ------------------------------------------------------
        """)

    except requests.ConnectionError:
        print(f"""\n
    ------------------------------------------------------
                    NO TIENES CONEXION!
    ------------------------------------------------------
        """)


got_pokemon()

input("\nPrsione cualquier tecla para salir...")
