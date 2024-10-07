# Pokédex Project

Este es un proyecto simple de una Pokédex que utiliza la API de [PokeAPI](https://pokeapi.co/) para obtener y mostrar la información de los Pokémon. La aplicación permite al usuario introducir el nombre de un Pokémon, obtener sus estadísticas e imagen, y almacenar la información en un archivo `.json`.

## Funcionalidades

- Permite al usuario buscar cualquier Pokémon por su nombre.
- Muestra la información básica del Pokémon, como:
  - **Peso** (convertido a kilogramos).
  - **Altura** (convertida a centímetros).
  - **Tipos** de Pokémon.
  - **Habilidades**.
  - **Movimientos** (solo se muestran los primeros 5 movimientos).
  - **Imagen frontal** del Pokémon.
- Si el Pokémon no es encontrado, se muestra un mensaje de error.
- La información obtenida se guarda en un archivo `.json` dentro de la carpeta `pokedex`.

## Requisitos

- Python 3.6 o superior.
- Biblioteca `requests` (puede ser instalada con `pip`).
- Conexión a Internet para acceder a la API de PokeAPI.

## Instalación

1. Clona el repositorio o descarga el código fuente.
2. Instala las dependencias necesarias ejecutando:

```bash
pip install requests
```

3. Ejecuta el programa:

```bash
python main.py
```

## Uso

1. Al ejecutar el programa, se te solicitará que ingreses el nombre de un Pokémon.
2. El programa buscará la información del Pokémon a través de la API de PokeAPI.
3. Si el Pokémon es encontrado, verás su información en la terminal, como peso, altura, tipos, habilidades y una imagen frontal.
4. La información también se almacenará en un archivo `.json` dentro de la carpeta `pokedex`.

## Estructura del Proyecto

- `main.py`: Contiene el código principal que gestiona la búsqueda y la visualización de la información del Pokémon.
- `pokedex/`: Carpeta donde se almacenan los archivos `.json` de cada Pokémon buscado.

## Ejemplo de Uso

```
Introduce el nombre del Pokémon: Bulbasaur

--- Información de Bulbasaur ---
Peso: 6.9 kg
Altura: 70.0 cm
Tipos: Grass, Poison
Habilidades: overgrow, chlorophyll
Movimientos: tackle, growl, leech-seed, vine-whip, poison-powder...
Imagen: https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png
Información guardada en pokedex/Bulbasaur.json
```

## Notas

- Si el Pokémon no existe, se mostrará un mensaje de error: `El Pokémon 'nombre' no fue encontrado.`
- El archivo `.json` generado contiene la información del Pokémon junto con el enlace a su imagen.

## Contribuciones

Si deseas contribuir a este proyecto, puedes hacerlo creando un _fork_ y enviando tus _pull requests_. Toda mejora y sugerencia es bienvenida.

## Créditos

Este proyecto utiliza la API de [PokeAPI](https://pokeapi.co/).

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
```

Este archivo `README.md` proporciona instrucciones claras sobre cómo instalar, usar y contribuir al proyecto de la Pokédex, así como una explicación detallada de la funcionalidad y estructura del código.