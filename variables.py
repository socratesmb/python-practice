# Variables de trabajo con buenas practicas.

Variable_Inicial = 'Cadena de texto'  # Escrito con Camel_Case.
print(Variable_Inicial)

variable_de_inicio = 'Cade de texto 2' # Escrito con snake_case, es mas recomendado.
print(variable_de_inicio)

variable_int = 7  # Ahora es una variable Int.
print(variable_int)

# Seria lo mismo para los diferentes tipos de variables.
#------------------------#

# Se le puede pasar multiples variables en el print.
print(Variable_Inicial, variable_de_inicio, '|', variable_int)

variable_int_to_str = str(variable_int)
print(variable_int_to_str) # Sigue siendo lo mismo visualmente
print(type(variable_int_to_str)) # Pero ahora se convirtio en string con la funcion str de la linea 19.

# Multiples variables en la misma linea, tener cuidado al usar esta creacion de variables.
name, surname, alias, age = 'Socrates', 'Martinez Berrio', 'SocratesMB' , 25
# Se puede inprimir o usar en el orden que quieras.
print("Hola, mucho gusto soy:", name, surname, ", tengo:", age, "y mi usuario de git es:", alias)