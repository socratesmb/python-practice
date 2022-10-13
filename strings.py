# String y sus diferentes formas de usarlos

from traceback import print_tb


my_string = 'Hola mundo!!!'
my_secod_string = 'Hello world!!!'

print(len(my_string), len(my_secod_string)) # Mostramos el tamaño de los string

my_string_salt = 'Este es un string\ncon salto de linea' # String con salto de linea con el comando \n
print(my_string_salt)

my_string_tab = '\tEste es otro string con tabulacion' # Este funciona con el comando \t
print(my_string_tab)

# Format string in code

name, surname, year, nick = "Socrates", "Martinez Berrio", 2022, "SocratesMB"

""" %s - Cadena (o cualquier objeto con una representación de cadena, como números)
    %d - Enteros
    %f - Números de punto flotante
"""

print("Hola coder mi nombre completo es %s %s y este codigo se hizo en %d" %(name, surname, year)) # Se imprime texto, pero se debe usar los modulos % correctos para ser leido
print("Hola coder mi nombre completo es {} {} y este codigo se hizo en {}".format(name, surname, year)) # Se imprime el texto, con la exepcion de que no necesita los modulos especificos
print(f"Hola coder mi nombre completo es {name} {surname} y este codigo se hizo en {year}") # Se hace por inferencia, pero es necesario agregar al inicio de la sentencia f

# Desempaquetado de caracteres
texto = "pythonn"
print(texto[::-1])
print(texto.upper())
print(texto.count('n'))
print(texto.lower())
print(texto.capitalize())