import time
import os

def borrarPantalla(): #Definimos la función borrar pantalla
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

# Función para solicitar una palabra al usuario
def solicitar_palabra():
    palabra = input("Introduce una palabra: ").strip()  # Pedir palabra y eliminar espacios en blanco adicionales
    return palabra

# Función para analizar la longitud de la palabra
def analizar_longitud_palabra(palabra):
    longitud = len(palabra)  # Obtener la longitud de la palabra
    
    # Condición para verificar si la palabra tiene entre 4 y 8 letras
    if 4 <= longitud <= 8:
        print(f"La palabra '{palabra}' es correcta. Tiene {longitud} letras.")
    
    # Si la palabra tiene menos de 4 letras
    elif longitud < 4:
        print(f"Hacen falta letras. Solo tiene {longitud} letras.")
    
    # Si la palabra tiene más de 8 letras
    else:
        print(f"Sobran letras. Tiene {longitud} letras.")

# Función principal que coordina el flujo del programa
def main():
    borrarPantalla()
    while True:  # Bucle para repetir la evaluación de palabras
        palabra = solicitar_palabra()  # Solicitar palabra al usuario
        analizar_longitud_palabra(palabra)  # Analizar y procesar la longitud de la palabra
        
        # Preguntar si se desea evaluar otra palabra
        otra = input("¿Quieres evaluar otra palabra? (s/n): ").strip().lower()
        
        # Si la respuesta no es 's', romper el ciclo y terminar el programa
        if otra != 's':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        borrarPantalla()        

# Llamada a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()
