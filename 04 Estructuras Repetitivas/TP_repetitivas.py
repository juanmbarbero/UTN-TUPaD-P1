"""Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""

for numero in range(0, 101):
    print(numero)
    
"""Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""

numero = input("Ingresa un número entero: ")
print("El número tiene", len(numero), "dígito(s).")

"""Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

print("La suma es:", sum(range(min(a, b) + 1, max(a, b))))

"""Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

suma_total = 0

numero = int(input("Ingresa un número entero (0 para terminar): "))

while numero != 0:
    suma_total += numero
    numero = int(input("Ingresa un número entero (0 para terminar): "))

print("El total acumulado es:", suma_total)

"""Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

import random

numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    
    if intento == numero_secreto:
        print(f"¡Felicitaciones! Adivinaste el número en {intentos} intentos.")
        break
    else:
        print("Intenta de nuevo.")

"""Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""

for numero in range(100, -1, -2):
    print(numero)

"""Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""

numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    suma = sum(range(numero + 1))
    print("La suma de todos los números entre 0 y", numero, "es:", suma)
    
"""Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

pares = impares = negativos = positivos = 0

for i in range(100):
    numero = input(f"Ingresa el número {i + 1} (o 'salir' para terminar): ")
    
    if numero.lower() == 'salir':
        break
    
    numero = int(numero)
    
    pares += numero % 2 == 0
    impares += numero % 2 != 0
    negativos += numero < 0
    positivos += numero > 0

print(f"\nPares: {pares}, Impares: {impares}, Negativos: {negativos}, Positivos: {positivos}")

"""Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""

cantidad = 100

suma = 0
contador = 0

for i in range(cantidad):
    entrada = input(f"Ingrese el número {i + 1} (o 'salir' para terminar): ")
    
    if entrada.lower() == "salir":
        break

    numero = int(entrada)
    suma += numero
    contador += 1

if contador > 0:
    media = suma / contador
    print(f"\nLa media de los {contador} número(s) ingresado(s) es: {media}")
else:
    print("\nNo se ingresaron números.")
    
"""Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

numero = input("Ingresa un número: ")
numero_invertido = numero[::-1]
print("Número invertido:", numero_invertido)

