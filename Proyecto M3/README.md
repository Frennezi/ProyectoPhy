Detalles del Funcionamiento:
Librerías Importadas:

random: Se utiliza para decidir aleatoriamente si una bola se mueve a la izquierda o a la derecha al chocar con un clavo.
matplotlib.pyplot: Se usa para generar gráficos que visualizan la distribución de las bolas en los compartimentos.
Función galton_simulation:

Entrada:
num_balls: Número de bolas que se dejarán caer.
num_rows: Número de filas de clavos por las que pasan las bolas.
Proceso:
Crea una lista llamada compartments con tantos elementos como filas de clavos + 1. Cada elemento en esta lista representa un compartimento donde se cuentan las bolas que caen en esa posición.
Por cada bola (representada en un bucle):
Inicia en la posición 0, que corresponde al primer compartimento (a la izquierda).
En cada fila, la bola se mueve aleatoriamente a la izquierda o derecha (con random.choice([0, 1])).
Una vez que la bola ha pasado por todas las filas, la posición final se incrementa en el compartimento correspondiente.
Este proceso se repite para todas las bolas.
Salida: Devuelve una lista compartments donde cada índice representa un compartimento y su valor indica cuántas bolas cayeron en ese compartimento.
Función plot_distribution:

Entrada: La lista compartments con los resultados de la simulación.
Proceso:
Utiliza matplotlib para crear un gráfico de barras. Cada barra representa un compartimento y su altura indica cuántas bolas cayeron en él.
Las etiquetas de los ejes x e y se definen como "Compartimentos" y "Número de bolas", respectivamente, para facilitar la lectura.
Finalmente, muestra la gráfica al usuario.
Salida: Una gráfica de barras que representa la distribución final de las bolas en los compartimentos.
Parámetros de Simulación:

num_balls: El programa define 3000 bolas que caerán por la máquina de Galton.
num_rows: Se establecen 12 filas de clavos, lo que crea 13 compartimentos posibles en la parte inferior.
Estos parámetros pueden ser modificados fácilmente para ajustar el número de bolas y filas en la simulación.
Ejecución:

El programa primero realiza la simulación llamando a galton_simulation con el número de bolas y filas.
Luego, pasa los resultados a la función plot_distribution para graficar la distribución.
Comportamiento Esperado:
Cuando se ejecuta este programa, las bolas caen a través de los clavos y se agrupan en compartimentos en la parte inferior. Debido a la forma en que las bolas se mueven de manera aleatoria a la izquierda o derecha en cada fila, la mayoría de las bolas terminarán cerca del centro, en compartimentos intermedios, mientras que pocas bolas llegarán a los compartimentos más alejados, lo que resulta en una distribución que se aproxima a la curva de Gauss o distribución normal.
