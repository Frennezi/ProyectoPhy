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
    # Obtiene la geometría de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Obtiene la geometría de la ventana gráfica
    window_width = 600
    window_height = 600

    # Calcula la posición centrada
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Establece la geometría de la ventana gráfica
    window.geometry(f'{window_width}x{window_height}+{x}+{y}')

def plot_point(x, y):
    import matplotlib.pyplot as plt  # Se asegura la importación de matplotlib

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

    # Plotea el punto
    plt.plot(x, y, 'ro')  # 'ro' indica un punto rojo
    plt.text(x, y, f'({x}, {y})', fontsize=12, ha='right')

    # Configura los límites de los ejes
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # Configura los títulos de los ejes
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')

    # Configura la ventana gráfica para estar centrada
    plt.show(block=False)  # block=False para no pausar el flujo del programa
    
    # Usa Tkinter para centrar la ventana
    center_window(root)

    # Pausa durante 6 segundos antes de cerrar el gráfico
    plt.pause(6)
    
    # Cierra el gráfico después de 6 segundos
    plt.close()

def main():
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
            print("Saliendo del programa.")
            break

if __name__ == "__main__":
    main()
