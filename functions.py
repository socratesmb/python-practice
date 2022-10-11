# Vamos a trabajar funciones

from numpy import square
from pygame import NUMEVENTS


def funccion():
    print("Hola developers!")

funccion()

# Las funciones pueden retornas diferentes tipos de valores

def funccion1():
    nombre = 'Socrates'
    apellido = 'Martinez'
    edad = 25
    correo = 'sberrio634@gmail.com'
    datos =  'Nombre: ' + nombre + ' Apellido: ' + apellido + ' Edad: ' + str(edad) + ' Email: ' + correo
    return datos

print(funccion1())

# Ingresando values en la funcion, desde datos simples a complejos

def operacion(x, y):
    return x * y

print(operacion(2, 9))

# Se puede retornar todo tipo de valores
'''
def positivo(n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False

s = int(input('Ingrese un numero: ')) # Recordar que cuando se ingrese un valor siempre es str, se debe setear al valor que necesitamos
print("El numero:", s, "es positivo:", positivo(s))
'''

# Se puede crear funciones con valores predeterminados de ser necesario

def peso_objeto(masa, gravedad = 9.81):
    peso = masa * gravedad
    return peso

print(peso_objeto(25)) # Se puede ingresar un solo valor y el segundo se toma por defecto
print(peso_objeto(25, 7.2)) # Se puede pasar los 2 valores 

# Se pueden tener funciones con numero de valores arbitrarios, osea no sabesmos cuantos se van a trabajar

def suma_numeros(*nums):
    r = 0
    for num in nums:
        r += num
    return r

print(suma_numeros(2)) # Podemos operar solo 1 numero
print(suma_numeros(2,3,4)) # Operar 2 numeros
print(suma_numeros(2,-2,3)) # Operar n numeros

# Tambien se puede crear funciones con parametros de otras funciones
def cuadrado_numero(n):
    return n * n

def operar_numero(f,x):
    return f(x)

print(operar_numero(cuadrado_numero, 4)) # Se concatena una funcion dentro de otra funcion, tener cuidado al ser creadas