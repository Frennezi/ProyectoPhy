import os
import requests
import json

# Directorio para guardar la información del Pokémon
POKEDEX_DIR = "pokedex"

# Crear la carpeta pokedex si no existe
if not os.path.exists(POKEDEX_DIR):
    os.makedirs(POKEDEX_DIR)

# Función para obtener la información del Pokémon
def obtener_info_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    response = requests.get(url)

    if response.status_code == 404:
        print(f"Error: El Pokémon '{nombre_pokemon}' no fue encontrado.")
        return None
    elif response.status_code != 200:
        print(f"Error: No se pudo obtener la información del Pokémon (Código {response.status_code}).")
        return None
    
    data = response.json()

    # Obtener las estadísticas necesarias
    pokemon_info = {
        "name": data["name"],
        "weight": data["weight"],
        "height": data["height"],
        "types": [t["type"]["name"] for t in data["types"]],
        "abilities": [a["ability"]["name"] for a in data["abilities"]],
        "moves": [m["move"]["name"] for m in data["moves"]],
        "image": data["sprites"]["front_default"]  # Imagen frontal
    }
    
    return pokemon_info

# Función para guardar los datos en un archivo JSON
def guardar_en_json(pokemon_info):
    nombre_archivo = f"{POKEDEX_DIR}/{pokemon_info['name']}.json"
    
    with open(nombre_archivo, "w") as f:
        json.dump(pokemon_info, f, indent=4)
    
    print(f"Información guardada en {nombre_archivo}")

# Función principal
def main():
    nombre_pokemon = input("Introduce el nombre del Pokémon: ").strip()
    info_pokemon = obtener_info_pokemon(nombre_pokemon)
    
    if info_pokemon:
        print(f"\n--- Información de {info_pokemon['name'].capitalize()} ---")
        print(f"Peso: {info_pokemon['weight']} decagramos")
        print(f"Altura: {info_pokemon['height']} decímetros")
        print(f"Tipos: {', '.join(info_pokemon['types'])}")
        print(f"Habilidades: {', '.join(info_pokemon['abilities'])}")
        print(f"Movimientos: {', '.join(info_pokemon['moves'][:5])}...")  # Mostrar solo los primeros 5 movimientos
        print(f"Imagen: {info_pokemon['image']}")
        
        # Guardar la información en un archivo JSON
        guardar_en_json(info_pokemon)
    else:
        print("No se pudo obtener la información del Pokémon.")

if __name__ == "__main__":
    main()
