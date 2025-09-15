import requests
from database import dbconnect

#TO DO
#lage nettside/display data på browser
#MBY lage slik at data blir hentet fra brukere på nettside. 



base_url = "https://pokeapi.co/api/v2/"

def add_to_db(pokemon_info):
    connection = dbconnect()
    if connection is None:
        print("womp womp no connection, cant add")
        return False
    try: 
        cursor = connection.cursor()
        query = """ INSERT INTO pokemon (id, pokémon, height, weight) VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (pokemon_info['id'], pokemon_info['name'], pokemon_info['height']/10, pokemon_info['weight']/10))
        connection.commit()
        return True
    except Exception as e:
        if 'Duplicate entry' in str(e):
            print("this pokemon is already in the database")
            return False
        else: 
            print(f"database error: {e}")
            return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("pokemon added to the database!")
  
def pokemon_exists(pokemon_name):
    connection = dbconnect()
    if connection is None:
        print("womp womp no connection, cant read")
        return False
    try:
        cursor = connection.cursor()
        query = "SELECT id FROM pokemon WHERE pokémon = %s"
        cursor.execute(query, (pokemon_name.lower(),))
        result = cursor.fetchone()
        return result is not None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
def pokemon_from_db(pokemon_name):
    connection = dbconnect()
    if connection is None:
        print("womp womp no connection, cant write")
    try: 
        cursor = connection.cursor(dictionary=True)
        query = "SELECT id, pokémon, height, weight FROM pokemon WHERE pokémon = %s"  
        cursor.execute(query, (pokemon_name.lower(),))    
        result = cursor.fetchone()
        return result
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()  
            
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

if not pokemon_exists(pokemon_name):
    pokemon_info = get_pokemon_info(pokemon_name)
    if pokemon_info:
        add_to_db(pokemon_info)
        print(f"Name: {pokemon_info["name"].capitalize()}")
        print(f"Id: {pokemon_info["id"]}")
        print(f"Height: {pokemon_info["height"]/10} M")
        print(f"Weight: {pokemon_info["weight"]/10} Kg")
        print("Pokemon gotten from Api")
else: 
    db_pokemon = pokemon_from_db(pokemon_name)
    if db_pokemon:
        print("From database:")
        print(f"Name: {pokemon_info["name"].capitalize()}")
        print(f"Id: {pokemon_info["id"]}")
        print(f"Height: {pokemon_info["height"]/10} M")
        print(f"Weight: {pokemon_info["weight"]/10} Kg")
