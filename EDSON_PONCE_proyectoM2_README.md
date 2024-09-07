Detalles de cómo se hizo el programa:
Función solicitar_palabra():

Esta función solicita al usuario que ingrese una palabra. Utilizamos la función input() para obtener la palabra, y la función strip() para eliminar posibles espacios en blanco antes o después de la palabra ingresada.
La palabra ingresada se devuelve al programa principal.
Función analizar_longitud_palabra(palabra):

Esta función toma la palabra ingresada como argumento.
Se utiliza len(palabra) para obtener la longitud de la palabra.
Luego, se evalúa la longitud de la palabra en tres condiciones:
Si la longitud está entre 4 y 8 letras (inclusive), se muestra un mensaje indicando que la palabra es correcta.
Si la longitud es menor de 4 letras, se muestra un mensaje indicando que faltan letras, y se informa cuántas letras tiene la palabra.
Si la longitud es mayor a 8 letras, se muestra un mensaje indicando que sobran letras, y se informa cuántas letras tiene la palabra.
Función main():

Esta función orquesta el flujo del programa. Primero llama a solicitar_palabra() para obtener la palabra del usuario, y luego llama a analizar_longitud_palabra() para verificar y procesar la longitud de la palabra.
Ejecución del programa:

Utilizamos if __name__ == "__main__": para asegurarnos de que el programa se ejecute solo cuando el archivo se ejecuta directamente, y no cuando se importa como módulo.
Esto inicia la ejecución de la función main().
Ejemplo de ejecución del programa:
Entrada: "sol"
Salida: "Hacen falta letras. Solo tiene 3 letras."
Entrada: "palabra"
Salida: "La palabra 'palabra' es correcta. Tiene 7 letras."
Entrada: "computadora"
Salida: "Sobran letras. Tiene 11 letras."