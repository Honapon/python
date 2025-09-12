import requests
from database import dbconnect

base_url = "https://pokeapi.co/api/v2/"

def add_to_db():
    connection = dbconnect()
    

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = input("choose a pokemon: ")
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]/10} M")
    print(f"Weight: {pokemon_info["weight"]/10} Kg")
#elif pokemon_info:
    