import os
import requests
import json
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO

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
        messagebox.showerror("Error", f"El Pokémon '{nombre_pokemon}' no fue encontrado.")
        return None
    elif response.status_code != 200:
        messagebox.showerror("Error", f"No se pudo obtener la información del Pokémon (Código {response.status_code}).")
        return None
    
    data = response.json()

    # Obtener las estadísticas necesarias y convertir peso/altura
    peso_kg = data["weight"] / 10  # Convertir de decagramos a kilogramos
    altura_cm = data["height"] * 10  # Convertir de decímetros a centímetros

    pokemon_info = {
        "name": data["name"],
        "weight": peso_kg,
        "height": altura_cm,
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
    
    messagebox.showinfo("Guardado", f"Información guardada en {nombre_archivo}")

# Función para mostrar la información del Pokémon en la interfaz
def mostrar_info():
    nombre_pokemon = entry_nombre.get().strip()
    
    if nombre_pokemon:
        info_pokemon = obtener_info_pokemon(nombre_pokemon)
        
        if info_pokemon:
            label_nombre.config(text=f"Nombre: {info_pokemon['name'].capitalize()}")
            label_peso.config(text=f"Peso: {info_pokemon['weight']} kg")
            label_altura.config(text=f"Altura: {info_pokemon['height']} cm")
            label_tipos.config(text=f"Tipos: {', '.join(info_pokemon['types'])}")
            label_habilidades.config(text=f"Habilidades: {', '.join(info_pokemon['abilities'])}")
            label_movimientos.config(text=f"Movimientos: {', '.join(info_pokemon['moves'][:5])}...")

            # Mostrar la imagen del Pokémon
            response = requests.get(info_pokemon["image"])
            img_data = Image.open(BytesIO(response.content))
            img_data = img_data.resize((150, 150))  # Redimensionar la imagen
            img = ImageTk.PhotoImage(img_data)
            label_imagen.config(image=img)
            label_imagen.image = img
            
            # Guardar la información en un archivo JSON
            guardar_en_json(info_pokemon)
    else:
        messagebox.showerror("Error", "Por favor, introduce el nombre de un Pokémon.")

# Crear la ventana principal
root = tk.Tk()
root.title("Pokédex")

# Crear los widgets
frame = tk.Frame(root)
frame.pack(pady=20)

label_title = tk.Label(frame, text="Introduce el nombre de un Pokémon", font=("Arial", 16))
label_title.grid(row=0, column=0, columnspan=2, pady=10)

entry_nombre = tk.Entry(frame, font=("Arial", 14))
entry_nombre.grid(row=1, column=0, columnspan=2, padx=10)

button_buscar = tk.Button(frame, text="Buscar", font=("Arial", 14), command=mostrar_info)
button_buscar.grid(row=2, column=0, columnspan=2, pady=10)

# Widgets para mostrar la información del Pokémon
label_imagen = tk.Label(frame)
label_imagen.grid(row=3, column=0, rowspan=4, padx=10)

label_nombre = tk.Label(frame, text="Nombre: ", font=("Arial", 12))
label_nombre.grid(row=3, column=1, sticky="w")

label_peso = tk.Label(frame, text="Peso: ", font=("Arial", 12))
label_peso.grid(row=4, column=1, sticky="w")

label_altura = tk.Label(frame, text="Altura: ", font=("Arial", 12))
label_altura.grid(row=5, column=1, sticky="w")

label_tipos = tk.Label(frame, text="Tipos: ", font=("Arial", 12))
label_tipos.grid(row=6, column=1, sticky="w")

label_habilidades = tk.Label(frame, text="Habilidades: ", font=("Arial", 12))
label_habilidades.grid(row=7, column=1, sticky="w")

label_movimientos = tk.Label(frame, text="Movimientos: ", font=("Arial", 12))
label_movimientos.grid(row=8, column=1, sticky="w")

# Iniciar la aplicación
root.mainloop()
