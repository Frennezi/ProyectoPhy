#Aqui es donde obtenemos la cantidad de personas
personas = int(input( "personas: "))

#Aqui verificamos que la cantidad sea mayor a 0 si no, no tiene sentido pedir nada
while personas > 0:
    #Le pedimos el nombre y lo guardamos en un input (Si usara Python 2.7 seria raw_input y no input pero usa python 3.7)
    n = input("Su nombre por favor: ")
    #Se pide al edad que siempre es un entero por eso el int() 
    e = int(input("Su edad en años por favor: "))
    #como la altura es en metros y no centimetros hay que ponerle punto y por ende es un flotante float()
    a = float(input ("Su altura en metros por favor: "))
    #Aqui se duplica codigo pero bueno... decimos que est (de estatura) es igual a altura (No me diga)
    est = a
    #La masa en kilogramos si puede tener decimales asi que la dejamos flotante
    m = float (input("Su masa en kilogramos por favor :"))
    #Calculo del IMC, masa (En kilogramos) entre la estatura (En metros) elevada al cuadrado
    IMC = m / est**2
    #Le decimos si es menor o mayor de edad, si es menor a 18 es menor, si no es mayor edad
    #Solo ruegue porque a nadie se le ocurra meter numeros negativos, le va a decir que es menor de edad
    if(e < 18):
        print("Usted es menor de edad")
    else:
        print("Usted es mayor de edad")
    #Le imprimos el IMC para que se ponga sad
    print("IMC: " + str(IMC) )

    #Hacemos las distintas validaciones
    if IMC >= 0 and IMC <= 15.99 :
        print ("Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print ("obesidad media")
    elif IMC >= 40.00:
        print ("obesidad morbida")

    #Por cada persona a la que le pedimos los datos debemos restarle una (Porque ya la recorrimos)
    #si no el ciclo se vuelve infinito
    personas = personas - 1
@Francisco331
Francisco331 commented on Dec 23, 2023
Hola amigo yo aun soy aprendiz de python y tome tu calculo de imc y le agregue algunos ootros conocimientos basicos por ejemplo que cuando diga cuanto IMC tienes en el print de los elif diga tambien la edad y el nombre, como aun soy aprendiz me gustaria que me dijeras o me dijeran si mi diseño para el calculo esta bien asi o lo puedo simplificar mas. Gracias

edad = int(input("Que edad tienes? "))
nombre = input("¿Como te llamas? ")
peso = float(input("¿Cuanto pesas en KG? "))
altura = float(input("¿Cuanto mides? "))

IMC = round(peso / altura ** 2)

if edad < 18:
print("eres menor de edad")

else:
print("Eres mayor de edad")

print("Masa Corporal " + str(IMC) )

if IMC >= 0 and IMC <= 16.99:
print("estas reflaco " + str(nombre) + " a tu edad de " + str(edad) + " deberias comer un poco mas por que tienes delgadez extrema")

elif IMC >= 17.00 and IMC <= 21.99:
print("estas avanzando " + str(nombre) + " a tu edad de " + str(edad) + " pero aun tienes delgadez solo que moderada")

elif IMC >= 22.00 and IMC <= 26.99:
print("Ahora si tu masa corporal es normal " + str(nombre) + "a tu edad de " + str(edad) + " estas en optimas condiciones")

elif IMC >= 27.00 and IMC <= 30.99:
print("estas engordando mucho " + str(nombre) + " a tu edad de " + str(edad) + " estas ya estas obeso")

elif IMC >= 31.00 and IMC <= 35.99:
print("diablo estas bien gordo " + str(nombre) + " a tu edad de " + str(edad) + " estas ya pareces tanque de guerra, has ejercicio")
