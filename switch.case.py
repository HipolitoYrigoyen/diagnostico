## Crea un programa que solicite al usuario ingresar un número del 1 al 7, representando cadadía de la semana (1 para lunes, 2 para martes, y así sucesivamente). Utiliza esta entrada para calcular y mostrar el nombre correspondiente al día de la semana.Pasos a seguir:1. Entrada de Datos:
## Solicita al usuario ingresar un número del 1 al 7.
## Cálculo del Día:
## Utiliza una estructura de control switch para determinar el nombre del día de la
## semana basándote en el número ingresado por el usuario. Asigna el nombre del día
## correspondiente a una variable.
## Salida de Resultados:
## Imprime en la pantalla el nombre del día de la semana calculado
## El ejercicio deberá ser realizado con if y elif ya que python no cuenta con switch.

numero = int(input("ingresá algún número del 1 al 7: "))
if numero == 1:
    print("El dia es: lunes") 

elif numero == 2:
    print("El dia es: martes")
elif numero == 3:
    print("El dia es: miercoles")
elif numero == 4:
    print("El dia es: jueves")
elif numero == 5:
    print("El dia es: viernes")
elif numero == 6:
    print("EL dia es: sabado")
elif numero == 7:
    print("EL dia es: domingo")
elif numero <= 0:
    print("Numero muy bajo, solo permitimos numeros del 1 al 7.")
elif numero >= 8:
    print("Numero muy alto, solo permitimos numeros del 1 al 7.")

