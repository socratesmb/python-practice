# Operadores en python

from numpy import true_divide


print(5+2)  # Suma
print(5-2)  # Resta
print(5*2)  # Multiplicacion
print(5/2)  # Division

print(10 % 2)  # Modulo, el resultado es el resto
print(11 // 2)  # Doble division aproximada
print(3**2)  # Exponente con 2 operadores de **

print('Numeros complejos:', 3 + 3j)  # Salida de numero complejos
print('Multiplicacion de numeros complejos: ', (1 + 1j)
      * (1 - 1j))  # Operacion de numeros complejos

# Creacion de variables numericas para operar
a = 3
b = 2

# Variables de almacenamiento de operadores
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# Impresion de variables resultantes
print(total)
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Operadores de comparacion, resultados en booleano

print(2 > 3)  # Mayor que
print(3 < 2)  # Menor que
print(7 <= 2)  # Menor igual
print(8 >= 1)  # Mayor igual
print(3 == 2)  # Igual si o si
print(3 != 2)  # Diferente de

# Se puede comparar caracteres de igual manera

print('Hola' > 'Python')  # Comparacion por caracteres
print('Hola' < 'Python')
print('Hola' >= 'Casa')  # Se comparan alfabeticamente en ASCII
print('Hola' <= 'Python')
print('Hola' == 'Hola')
print('Hola' != 'Python')

# Operadores Logicos

print(2 < 4 and 1 > 3)  # And, y, &&
print(3 <= 2 or 3 >= 2)  # Or, o, ||
print(not True)  # Operador no
print(not False)  # Se usa para negar la operacion
print(not not True)
print(not not False)


for i in [1, 2, 3, 4, 5]:
    print(i, end=" ")
    for j in [0, 1, 2, 3]:
        x = i**j
        print(x, end=" ")
    print("")