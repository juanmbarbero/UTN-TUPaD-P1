"""Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
función para calcular y mostrar en pantalla el factorial de todos los números enteros 
entre 1 y el número que indique el usuario"""

def factorial(n):
  
  if n <= 1:
    return 1
  
  return n * factorial(n - 1)

try:
  
  limite = int(input("Calcular factoriales hasta el número: "))

  if limite > 0:
    for i in range(1, limite + 1):
      print(f"El factorial de {i} es {factorial(i)}")
  else:
    print("Por favor, ingrese un número mayor que 0.")

except ValueError:
  print("Error: Debe ingresar un número entero.")
  
"""Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
especifique."""

def fibonacci(pos):
  if pos <= 1:
    return pos
  return fibonacci(pos - 1) + fibonacci(pos - 2)

try:
  limite = int(input("Mostrar la serie de Fibonacci hasta la posición: "))

  if limite >= 0:
    print("Serie de Fibonacci:")
    for i in range(limite + 1):
      print(fibonacci(i), end=" ")
    print()
  else:
    print("Por favor, ingrese una posición mayor o igual a 0.")

except ValueError:
  print("Error: Debe ingresar un número entero.")
  
"""Crea una función recursiva que calcule la potencia de un número base elevado a un 
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
algoritmo general."""

def calcular_potencia(base, exponente):
  if exponente == 0:
    return 1
  else:
    return base * calcular_potencia(base, exponente - 1)

try:
  num_base = float(input("Ingrese el número base: "))
  num_exponente = int(input("Ingrese el exponente (entero no negativo): "))

  if num_exponente < 0:
    print("Error: El exponente debe ser un número entero no negativo.")
  else:
    resultado = calcular_potencia(num_base, num_exponente)
    print(f"Resultado: {num_base} elevado a la {num_exponente} es {resultado}")

except ValueError:
  print("Error: Ingrese números válidos.")
  
"""Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
lo es. 
     Requisitos: 
La solución debe ser recursiva. 
No se debe usar [::-1] ni la función reversed()."""

def es_palindromo(palabra):
  if len(palabra) <= 1:
    return True
  
  return palabra[0] == palabra[-1] and es_palindromo(palabra[1:-1])

print(f"reconocer -> {es_palindromo('reconocer')}")
print(f"neuquen   -> {es_palindromo('neuquen')}")
print(f"python    -> {es_palindromo('python')}")
print(f"a         -> {es_palindromo('a')}")
print(f"rotor     -> {es_palindromo('rotor')}")
print(f"casa      -> {es_palindromo('casa')}")

"""Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
número entero positivo y devuelva la suma de todos sus dígitos. 
     Restricciones: 
No se puede convertir el número a string. 
Usá operaciones matemáticas (%, //) y recursión. 
Ejemplos: 
suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
suma_digitos(9)      → 9 
suma_digitos(305)    → 8   (3 + 0 + 5)"""

def suma_digitos(n):
  if n < 10:
    return n
  return (n % 10) + suma_digitos(n // 10)

print(f"Suma de los dígitos de 1234 -> {suma_digitos(1234)}")
print(f"Suma de los dígitos de 9    -> {suma_digitos(9)}")
print(f"Suma de los dígitos de 305  -> {suma_digitos(305)}")
print(f"Suma de los dígitos de 987  -> {suma_digitos(987)}")