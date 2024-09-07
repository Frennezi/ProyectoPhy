# ProyectoPhy
Tareas de UCamp
1. Funciones principales
solicitar_dato()
Esta función se encarga de solicitar un dato al usuario y valida su entrada. Tiene dos variantes:

Si se espera un número (como peso, estatura o edad), valida que el dato sea un número positivo.
Si no se espera un número, simplemente verifica que no esté vacío.
También hay un límite de intentos (3 intentos), y si el usuario no ingresa un valor válido, el programa se cierra con sys.exit().
calcular_imc()
Esta función recibe como parámetros el peso y la estatura del usuario, y usa la fórmula para calcular el Índice de Masa Corporal (IMC):

python
IMC = peso / (estatura ** 2)
Donde el peso está en kilogramos y la estatura en metros.

clasificar_imc()
Una vez calculado el IMC, esta función clasifica el resultado de acuerdo con las categorías de salud (bajo peso, peso normal, sobrepeso, obesidad). Dependiendo del valor del IMC, retorna una cadena con la clasificación correspondiente:

IMC < 18.5: Bajo peso
IMC entre 18.5 y 24.9: Peso normal
IMC entre 25 y 29.9: Sobrepeso
IMC ≥ 30: Obesidad
mostrar_animacion()
Simula un proceso de cálculo con una barra de progreso. Muestra un patrón visual ([###.....]) que se va llenando poco a poco para simular que el programa está calculando el IMC.

mostrar_resultado()
Una vez que el IMC ha sido calculado y clasificado, esta función muestra los datos proporcionados por el usuario, junto con el resultado del IMC y su clasificación. Además, se muestra el peso y la estatura con dos decimales para mayor precisión:

python
print(f"Índice de Masa Corporal (IMC): {imc:.2f}")
realizar_otra_operacion()
Después de mostrar los resultados, esta función pregunta al usuario si desea calcular otro IMC. Valida que la respuesta sea "s" (sí) o "n" (no). Si elige "s", el programa vuelve a comenzar el proceso de solicitud de datos; si elige "n", el programa finaliza.

mostrar_historial()
Cuando el usuario termina de hacer cálculos, se le pregunta si quiere ver el historial. Esta función toma la lista historial (que contiene todos los cálculos de IMC realizados en la sesión) y la muestra con el mismo formato detallado que se utilizó para los cálculos individuales.

2. Estructura del flujo del programa
El flujo principal del programa está controlado por un bucle while True en la función main(). Dentro del bucle:

Se solicita al usuario su nombre, apellido paterno, apellido materno, edad, peso, y estatura.
Luego se calcula el IMC y se clasifica.
El resultado se muestra detalladamente.
Finalmente, se le pregunta al usuario si desea realizar otro cálculo o ver el historial.
Historial
El historial de resultados se guarda en la lista historial. Cada vez que se realiza un cálculo de IMC, los datos completos se guardan como una tupla con esta estructura:

python
Copiar código
(nombre, apellido_paterno, apellido_materno, edad, peso, estatura, imc, clasificacion)
Esto permite que al final de la sesión, se muestre un registro detallado de todos los cálculos realizados.

3. Pruebas unitarias
Clase TestIMCFunctions
Esta clase contiene pruebas unitarias para verificar que la función clasificar_imc() funciona correctamente. Se prueban distintos valores de IMC para asegurar que:

Un IMC de 17 se clasifica como "Bajo peso".
Un IMC de 22 se clasifica como "Peso normal".
Un IMC de 27 se clasifica como "Sobrepeso".
Un IMC de 31 se clasifica como "Obesidad".
También se prueban los valores límite (IMC de 18.5, 24.9 y 29.9) para verificar que se asignen correctamente a sus respectivas categorías.
Las pruebas se ejecutan automáticamente cuando el programa es ejecutado, antes de comenzar la ejecución del flujo principal.

4. Detalles adicionales
Formato del historial: Cuando el historial de cálculos se muestra, los datos se formatean cuidadosamente, mostrando los valores numéricos con dos decimales y utilizando una estructura clara y ordenada:
python
Copiar código
print(f"{index}. {nombre} {apellido_paterno} {apellido_materno} - Edad: {edad} años - "
      f"Peso: {peso:.2f} kg - Estatura: {estatura:.2f} m - IMC: {imc:.2f} ({clasificacion})")
      
Resumen:
Este programa pide al usuario datos personales y calcula su IMC. El usuario puede realizar múltiples cálculos en una misma sesión, y al final se le ofrece la opción de ver el historial detallado de todos los cálculos realizados. El programa utiliza animaciones simples, manejo de errores en la entrada de datos y pruebas automatizadas para asegurar el correcto funcionamiento de las funciones clave.