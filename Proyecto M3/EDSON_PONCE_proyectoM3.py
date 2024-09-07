import random
import matplotlib.pyplot as plt

def galton_simulation(num_balls, num_rows):
    # Crear los compartimentos de acuerdo al número de filas
    compartments = [0] * (num_rows + 1)  # Inicializa los compartimentos en cero
    
    # Simulamos el movimiento de cada bola
    for _ in range(num_balls):
        position = 0  # Comienza en la posición 0 (compartimento más a la izquierda)
        for _ in range(num_rows):
            position += random.choice([0, 1])  # Elige aleatoriamente moverse a la izquierda (0) o a la derecha (1)
        compartments[position] += 1  # Incrementa el compartimento correspondiente
    
    return compartments  # Devuelve la distribución de bolas en los compartimentos

def plot_distribution(compartments):
    # Graficar la distribución
    plt.bar(range(len(compartments)), compartments, color='blue')  # Crea un gráfico de barras
    plt.xlabel('Compartimentos')  # Etiqueta del eje x
    plt.ylabel('Número de bolas')  # Etiqueta del eje y
    plt.title('Distribución de la máquina de Galton')  # Título del gráfico
    plt.show()  # Muestra el gráfico

# Parámetros de la simulación
num_balls = 3000  # Número de bolas que se dejarán caer
num_rows = 12     # Número de filas de clavos

# Simulación y visualización
compartments = galton_simulation(num_balls, num_rows)  # Realiza la simulación
plot_distribution(compartments)  # Grafica la distribución resultante
