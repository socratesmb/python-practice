# Trabajaremos modulos

from random import random
import functions as fc

print('-------------')
print(fc.peso_objeto(62)) # Se importa todo el documento y ejecuta todo lo que tiene

from functions import peso_objeto as ps

print('----------')
print(ps(61)) # Aca se importa solo la funcion que queremos usar

# Con python se puede importar muchas librerias como sys

#import sys
#print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))


# Se puede importar tambien librerias como statistics para datos estadisticos
print('----------')
import statistics as st

edades = [21,32,45,32,10,29,67,11,17,35]
print(st.mean(edades)) # Media
print(st.median(edades)) # Mediana
print(st.mode(edades)) # Moda
print(st.stdev(edades)) # Desviacion estandar

# Tambien librerias como math para datos matematicos

print('----------')
import math

print(math.pi) # Valor de pi
print(math.sqrt(2)) # Cuadrado
print(math.pow(2, 8)) # Exponencial
print(math.floor(17.92)) # Redondeo al menor
print(math.ceil(17.92)) # Redondeo al mayor
print(math.log10(100)) # Logaritmo en base 10

# Tambien podemos importar modulo de cadenas

print('----------')
import string as st

print(st.ascii_letters) # abecedario
print(st.digits) # numeros
print(st.punctuation) # Caracteres especiales

# Tambien importar el modulo random

print('----------')
import random as rd

print(rd.random()) # Aleaterio 
print(rd.randint(7, 17)) # Aletatorio entre intervalos