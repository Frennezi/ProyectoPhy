import unittest
import time
import sys
import os

def borrarPantalla(): #Definimos la función borrar pantalla
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def solicitar_dato(mensaje, es_numerico=False):
    intentos = 3  # Máximo 3 intentos para cada dato
    while intentos > 0:
        dato = input(mensaje).strip()
        if not dato:
            print(f"Este campo no puede quedar vacío. Intentos restantes: {intentos - 1}")
        elif es_numerico:
            try:
                dato = float(dato)
                if dato <= 0:
                    print(f"El valor debe ser mayor a 0. Intentos restantes: {intentos - 1}")
                else:
                    return dato
            except ValueError:
                print(f"Debes introducir un número válido. Intentos restantes: {intentos - 1}")
        else:
            return dato
        intentos -= 1
    print("Has excedido el número de intentos. El programa se cerrará.")
    sys.exit()  # Finalizar el programa si hay demasiados errores

def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

# Corregida la función para manejar límites de clasificación
def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc <= 24.9:  # Incluye límite superior
        return "Peso normal"
    elif 25 <= imc <= 29.9:  # Incluye límite superior
        return "Sobrepeso"
    else:
        return "Obesidad"

def mostrar_animacion():
    print("Calculando IMC...")
    barra = ['[          ]', '[#         ]', '[##        ]', '[###       ]', '[####      ]', 
             '[#####     ]', '[######    ]', '[#######   ]', '[########  ]', '[######### ]', '[##########]']
    for i in barra:
        sys.stdout.write(f"\r{i}")
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n")

def mostrar_resultado(nombre, apellido_paterno, apellido_materno, edad, peso, estatura, imc, clasificacion):
    mostrar_animacion()
    borrarPantalla()
    print("\n--- Información proporcionada ---")
    print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso:.2f} kg")
    print(f"Estatura: {estatura:.2f} m")
    print(f"Índice de Masa Corporal (IMC): {imc:.2f}")
    print(f"Clasificación de IMC: {clasificacion}")
    print("-----------------------------------")

def realizar_otra_operacion():
    while True:
        respuesta = input("¿Deseas calcular otro IMC? (s/n): ").lower().strip()
        if respuesta == 's':
            borrarPantalla()
            return True
        elif respuesta == 'n':
            return False
        else:
            print("Respuesta no válida. Por favor, introduce 's' para sí o 'n' para no.")
    

def mostrar_historial(historial):
    borrarPantalla()
    if len(historial) == 0:
        print("No hay cálculos en el historial.")
    else:
        print("\n--- Historial de cálculos ---")
        for index, registro in enumerate(historial, 1):
            nombre, apellido_paterno, apellido_materno, edad, peso, estatura, imc, clasificacion = registro
            print(f"{index}. {nombre} {apellido_paterno} {apellido_materno} - Edad: {edad} años - "
                  f"Peso: {peso:.2f} kg - Estatura: {estatura:.2f} m - IMC: {imc:.2f} ({clasificacion})")
        print("----------------------------")

def main():
    historial = []
    while True:
        nombre = solicitar_dato("Introduce tu nombre: ")
        apellido_paterno = solicitar_dato("Introduce tu apellido paterno: ")
        apellido_materno = solicitar_dato("Introduce tu apellido materno: ")
        edad = solicitar_dato("Introduce tu edad: ", es_numerico=True)
        peso = solicitar_dato("Introduce tu peso en kilogramos: ", es_numerico=True)
        estatura = solicitar_dato("Introduce tu estatura en metros: ", es_numerico=True)

        imc = calcular_imc(peso, estatura)
        clasificacion = clasificar_imc(imc)

        mostrar_resultado(nombre, apellido_paterno, apellido_materno, edad, peso, estatura, imc, clasificacion)

        resultado = (nombre, apellido_paterno, apellido_materno, edad, peso, estatura, imc, clasificacion)
        historial.append(resultado)

        if not realizar_otra_operacion():
            break

    while True:
        ver_historial = input("¿Deseas ver el historial de cálculos? (s/n): ").lower().strip()
        if ver_historial == 's':
            mostrar_historial(historial)
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        elif ver_historial == 'n':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Respuesta no válida. Por favor, introduce 's' para sí o 'n' para no.")

class TestIMCFunctions(unittest.TestCase):

    def test_clasificar_imc_bajo_peso(self):
        self.assertEqual(clasificar_imc(17), "Bajo peso")

    def test_clasificar_imc_peso_normal(self):
        self.assertEqual(clasificar_imc(22), "Peso normal")

    def test_clasificar_imc_sobrepeso(self):
        self.assertEqual(clasificar_imc(27), "Sobrepeso")

    def test_clasificar_imc_obesidad(self):
        self.assertEqual(clasificar_imc(31), "Obesidad")

    def test_clasificar_imc_limite_bajo_peso(self):
        self.assertEqual(clasificar_imc(18.5), "Peso normal")

    def test_clasificar_imc_limite_peso_normal(self):
        self.assertEqual(clasificar_imc(24.9), "Peso normal")

    def test_clasificar_imc_limite_sobrepeso(self):
        self.assertEqual(clasificar_imc(29.9), "Sobrepeso")

if __name__ == "__main__":
    unittest.main(exit=False)
    time.sleep(0.5)
    borrarPantalla()
    main()
