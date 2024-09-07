import subprocess
import sys
import matplotlib.pyplot as plt # type: ignore
import tkinter as tk
import time
import os

def borrarPantalla(): #Definimos la función borrar pantalla
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def check_and_install_matplotlib():
    """
    Verifica si matplotlib está instalada. Si no está instalada, intenta instalarla.
    """
    try:
        # Intenta importar matplotlib para verificar si está instalada
        import matplotlib.pyplot as plt # type: ignore
        print("matplotlib ya está instalada.")
    except ImportError:
        # Si no está instalada, intenta instalarla
        print("matplotlib no está instalada. Intentando instalar...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
            # Intenta importar nuevamente después de la instalación
            import matplotlib.pyplot as plt # type: ignore
            print("Instalación completada exitosamente.")
        except subprocess.CalledProcessError as e:
            print("Error al intentar instalar matplotlib.")
            print(f"Detalles del error: {e}")
            sys.exit(1)  # Sale del programa con un código de error

def center_window(window):
    """
    Centra la ventana gráfica en la pantalla.
    
    :param window: Objeto de ventana gráfica de Tkinter.
    """
    # Obtiene la geometría de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Establece el tamaño de la ventana gráfica
    window_width = 600
    window_height = 600

    # Calcula la posición centrada
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Establece la geometría de la ventana gráfica
    window.geometry(f'{window_width}x{window_height}+{x}+{y}')

def plot_point(x, y):
    """
    Muestra un gráfico con el punto (x, y) y ajusta los límites para que el punto siempre esté visible.
    
    :param x: Coordenada X del punto.
    :param y: Coordenada Y del punto.
    """
    import matplotlib.pyplot as plt  # type: ignore # Se asegura la importación de matplotlib

    # Cierra cualquier gráfico anterior
    plt.close()

    # Crea una ventana gráfica de Tkinter
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter

    # Configura el gráfico
    fig = plt.figure(figsize=(6, 6))
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, which='both')

    # Define un margen alrededor del punto para mantenerlo visible
    margin = 0.5
    x_margin = margin
    y_margin = margin

    # Ajusta los límites del gráfico para que el punto siempre esté dentro del área visible
    plt.xlim(x - x_margin, x + x_margin)
    plt.ylim(y - y_margin, y + y_margin)

    # Plotea el punto
    plt.plot(x, y, 'ro')  # 'ro' indica un punto rojo
    plt.text(x, y, f'({x}, {y})', fontsize=12, ha='right')

    # Configura los títulos de los ejes
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')

    # Muestra el gráfico
    plt.title('Visualización de Coordenadas')
    plt.show(block=False)  # block=False para no pausar el flujo del programa
    
    # Usa Tkinter para centrar la ventana
    center_window(root)

    # Pausa durante 10 segundos antes de cerrar el gráfico
    plt.pause(10)
    
    # Cierra el gráfico después de 10 segundos
    plt.close()

def analyze_coordinates():
    """
    Permite al usuario ingresar coordenadas y determina en qué cuadrante se encuentra el punto.
    Muestra el punto en un gráfico y permite ingresar múltiples coordenadas.
    """
    # Verifica si matplotlib está instalado o no
    check_and_install_matplotlib()

    while True:  # Bucle para permitir ingresar múltiples coordenadas
        borrarPantalla()
        try:
            # Solicita al usuario que ingrese las coordenadas X e Y
            x = float(input("Ingrese X: "))
            y = float(input("Ingrese Y: "))

            # Verifica que ninguna de las coordenadas sea 0
            if x == 0 or y == 0:
                print("Error: Ninguna de las coordenadas puede ser 0.")
            else:
                # Determina en cuál de los cuatro cuadrantes se encuentra el punto
                if x > 0 and y > 0:
                    print("El punto se encuentra en el cuadrante I")
                elif x < 0 and y > 0:
                    print("El punto se encuentra en el cuadrante II")
                elif x < 0 and y < 0:
                    print("El punto se encuentra en el cuadrante III")
                elif x > 0 and y < 0:
                    print("El punto se encuentra en el cuadrante IV")

                # Muestra la coordenada gráficamente
                plot_point(x, y)
        except ValueError:
            print("Error: Por favor, ingrese valores numéricos válidos.")

        # Pregunta si el usuario desea ingresar otra coordenada
        again = input("¿Desea ingresar otra coordenada? (s/n): ").strip().lower()
        if again != 's':
            break

# Función para solicitar una palabra al usuario
def solicitar_palabra():
    palabra = input("Introduce una palabra: ").strip()  # Pedir palabra y eliminar espacios en blanco adicionales
    return palabra

# Función para analizar la longitud de la palabra
def analyze_palabra(palabra):
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

def count_words():
    """
    Permite al usuario ingresar una frase y cuenta el número de palabras en la frase.
    Permite ingresar múltiples frases.
    """
    while True:  # Bucle para repetir la evaluación de palabras
        borrarPantalla()
        try:
            palabra = solicitar_palabra()  # Solicitar palabra al usuario
            analyze_palabra(palabra)  # Analizar y procesar la longitud de la palabra
        
            # Preguntar si se desea evaluar otra palabra
            otra = input("¿Quieres evaluar otra palabra? (s/n): ").strip().lower()
        except Exception as e:
            print(f"Error: {e}")
        # Si la respuesta no es 's', romper el ciclo
        if otra != 's':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

def main():
    """
    Muestra un menú para que el usuario elija entre analizar coordenadas o contar palabras.
    Ejecuta el programa seleccionado y permite regresar al menú después de cada opción.
    """
    while True:
        borrarPantalla()
        print("Seleccione el programa que desea ejecutar:")
        print("1. Analizar coordenadas")
        print("2. Contar palabras en una frase")
        print("3. Salir")

        choice = input("Ingrese el número de su elección (1, 2 o 3): ").strip()

        if choice == '1':
            borrarPantalla()
            analyze_coordinates()
        elif choice == '2':
            borrarPantalla()
            count_words()
        elif choice == '3':
            print("Saliendo del programa.")
            sys.exit(0)  # Sale del programa con un código de éxito
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
            time.sleep(2)
            borrarPantalla()

if __name__ == "__main__":
    main()
