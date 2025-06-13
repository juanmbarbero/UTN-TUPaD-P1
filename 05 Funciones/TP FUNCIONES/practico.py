"""Crear una función llamada imprimir_hola_mundo que imprima por
 pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
 programa principal."""
 
def imprimir_hola_mundo():
   
    print("Hola Mundo!")

if __name__ == "__main__":
    print("Llamando a la función desde el programa principal.")
    imprimir_hola_mundo()

"""Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
Llamar a esta función desde el programa principal solicitando el nombre al usuario."""

def saludar_usuario(nombre):
    return f"Hola {nombre}!"


if __name__ == "__main__":
    print(saludar_usuario(input("Introduce tu nombre: ")))
    

"""Crear una función llamada informacion_personal(nombre, apellido,
 edad, residencia) que reciba cuatro parámetros e imprima: “Soy
 [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario
y llamar a esta función con los valores ingresados."""

def informacion_personal(nombre, apellido, edad, residencia):
    """Imprime un resumen con los datos proporcionados."""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


if __name__ == "__main__":
    
    informacion_personal(
        input("Nombre: "),
        input("Apellido: "),
        input("Edad: "),
        input("Residencia: ")
    )
    
"""Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro 
y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva
el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados."""

import math

def calcular_area_circulo(radio):
    """Devuelve el área de un círculo (π * r²)."""
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    """Devuelve el perímetro de un círculo (2 * π * r)."""
    return 2 * math.pi * radio


if __name__ == "__main__":
    
    radio_usuario = float(input("Introduce el radio del círculo: "))

    print(f"Área: {calcular_area_circulo(radio_usuario):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio_usuario):.2f}")
    

"""Crear una función llamada segundos_a_horas(segundos) que reciba
 una cantidad de segundos como parámetro y devuelva la cantidad
 de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función."""

def segundos_a_horas(segundos):
    """Convierte una cantidad de segundos a horas."""
    
    return segundos / 3600


if __name__ == "__main__":
    
    segundos_usuario = int(input("Introduce la cantidad de segundos: "))

    horas = segundos_a_horas(segundos_usuario)
    print(f"{segundos_usuario} segundos equivalen a {horas:.2f} horas.")
    
"""Crear una función llamada tabla_multiplicar(numero) que reciba un
 número como parámetro y imprima la tabla de multiplicar de ese
 número del 1 al 10. Pedir al usuario el número y llamar a la función."""

def tabla_multiplicar(numero):
    """
    Imprime la tabla de multiplicar del 1 al 10 para el número dado.
    """
    print(f"--- Tabla del {numero} ---")
    
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


if __name__ == "__main__":
    
    num_usuario = int(input("Introduce un número para ver su tabla: "))
    
    tabla_multiplicar(num_usuario)

"""Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resulta
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara."""

def operaciones_basicas(a, b):
    
    if b == 0:
        division = "Error: División por cero"
    else:
        division = a / b
        
    return (a + b, a - b, a * b, division)


if __name__ == "__main__":
    
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    suma, resta, multiplicacion, division = operaciones_basicas(num1, num2)

    print("\n--- Resultados ---")
    print(f"Suma:          {suma}")
    print(f"Resta:         {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División:      {division}")
    
"""Crear una función llamada calcular_imc(peso, altura) que reciba el
 peso en kilogramos y la altura en metros, y devuelva el índice de
 masa corporal (IMC). Solicitar al usuario los datos y 
 llamar a la función para mostrar el resultado con dos decimales."""
 
def calcular_imc(peso, altura):
   
    if altura == 0:
        return 0
    return peso / (altura ** 2)


if __name__ == "__main__":
   
    peso_usuario = float(input("Introduce tu peso en kg: "))
    altura_usuario = float(input("Introduce tu altura en metros (ej: 1.75): "))

    imc = calcular_imc(peso_usuario, altura_usuario)

    print(f"\nTu Índice de Masa Corporal (IMC) es: {imc:.2f}")
    
"""Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
 una temperatura en grados Celsius y devuelva su equivalente en
 Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
 resultado usando la función."""

def celsius_a_fahrenheit(celsius):
   
    return (celsius * 9/5) + 32


if __name__ == "__main__":

    temp_celsius = float(input("Introduce la temperatura en grados Celsius: "))

    temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)

    print(f"{temp_celsius:.1f}°C equivale a {temp_fahrenheit:.1f}°F.")
    
"""Crear una función llamada calcular_promedio(a, b, c) que reciba
 tres números como parámetros y devuelva el promedio de ellos.
 Solicitar los números al usuario y mostrar el resultado usando esta
 función."""
 
def calcular_promedio(a, b, c):
   
    return (a + b + c) / 3


if __name__ == "__main__":

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    num3 = float(input("Introduce el tercer número: "))

    promedio = calcular_promedio(num1, num2, num3)

    print(f"\nEl promedio de los tres números es: {promedio:.2f}")


 

 
