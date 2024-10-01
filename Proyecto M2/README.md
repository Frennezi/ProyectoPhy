### Descripción del Programa

Este programa combina dos funcionalidades principales:
1. **Analizar Coordenadas**: Permite ingresar coordenadas (X, Y), determina el cuadrante del punto y muestra el punto en un gráfico ajustado para que siempre sea visible.
2. **Contar Palabras**: Permite ingresar una palabra y analiza su longitud para determinar si cumple con ciertos criterios.

Además, el programa incluye un menú principal que permite al usuario elegir entre estas funcionalidades o salir del programa.

### Componentes del Programa

1. **Importaciones**:
   - `subprocess`, `sys`, `matplotlib.pyplot`, `tkinter`, `time`, y `os` se utilizan para instalar paquetes, manejar la interfaz gráfica, y gestionar la consola.

2. **Funciones de Utilidad**:
   - **`borrarPantalla()`**:
     - Limpia la pantalla de la consola. Usa `os.system()` para ejecutar el comando correspondiente dependiendo del sistema operativo (`clear` para Unix y `cls` para Windows).

3. **Verificación e Instalación de `matplotlib`**:
   - **`check_and_install_matplotlib()`**:
     - Verifica si `matplotlib` está instalada. Si no lo está, intenta instalarla. Si la instalación falla, el programa se cierra con un código de error.

4. **Centrado de la Ventana Gráfica**:
   - **`center_window(window)`**:
     - Centra la ventana gráfica de Tkinter en la pantalla calculando las posiciones adecuadas basándose en el tamaño de la ventana y de la pantalla.

5. **Mostrar el Gráfico**:
   - **`plot_point(x, y)`**:
     - Muestra un gráfico con el punto `(x, y)`. Ajusta los límites del gráfico para que el punto siempre esté visible, centra la ventana gráfica y mantiene el gráfico visible durante 10 segundos.

6. **Funcionalidad de Análisis de Coordenadas**:
   - **`analyze_coordinates()`**:
     - Solicita coordenadas X e Y del usuario, verifica que no sean 0, determina en qué cuadrante se encuentra el punto y muestra el gráfico correspondiente. Permite ingresar múltiples coordenadas y regresar al menú principal después de cada entrada.

7. **Funcionalidad de Conteo de Palabras**:
   - **`solicitar_palabra()`**:
     - Solicita una palabra al usuario.
   - **`analyze_palabra(palabra)`**:
     - Analiza la longitud de la palabra ingresada y verifica si está en el rango de 4 a 8 letras. Proporciona retroalimentación sobre la longitud de la palabra.
   - **`count_words()`**:
     - Permite ingresar una palabra y usa `analyze_palabra()` para evaluar su longitud. Permite evaluar múltiples palabras y regresar al menú principal después de cada entrada.

8. **Menú Principal**:
   - **`main()`**:
     - Muestra un menú con opciones para analizar coordenadas, contar palabras o salir del programa. Dependiendo de la selección del usuario, ejecuta la función correspondiente (`analyze_coordinates()` o `count_words()`). Permite regresar al menú principal después de completar una opción.

### Flujo del Programa

1. **Inicio del Programa**:
   - Se inicia el programa y se ejecuta la función `main()` para mostrar el menú de opciones.

2. **Selección de Opción**:
   - El usuario elige entre analizar coordenadas, contar palabras o salir del programa.

3. **Ejecución de la Opción Seleccionada**:
   - **Para analizar coordenadas**:
     - El usuario ingresa coordenadas.
     - El programa determina el cuadrante y muestra el punto en un gráfico ajustado para visibilidad.
     - Después de mostrar el gráfico, el programa regresa al menú principal.
   - **Para contar palabras**:
     - El usuario ingresa una palabra.
     - El programa analiza la longitud de la palabra y muestra un mensaje basado en los criterios establecidos.
     - Después de analizar la palabra, el programa regresa al menú principal.

4. **Salir del Programa**:
   - Si el usuario selecciona la opción de salir, el programa termina de manera limpia.

### Comentarios Adicionales

- **Manejo de Errores**:
  - Incluye manejo básico de errores para entradas no válidas y errores en la instalación de paquetes.
  
- **Interactividad**:
  - Permite al usuario realizar múltiples acciones antes de salir, haciendo el programa interactivo y flexible.

- **Modularidad**:
  - La división en funciones facilita la estructura del código, su mantenimiento y extensión futura.

Este enfoque modular y basado en funciones asegura que el programa sea eficiente, fácil de entender y mantener, y proporciona una experiencia de usuario fluida y dinámica.
