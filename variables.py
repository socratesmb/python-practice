# Variables de trabajo con buenas practicas.

Variable_Inicial = 'Cadena de texto'  # Escrito con camelcase.
print(Variable_Inicial)

variable_de_inicio = 'Cade de texto 2' # Escrito con snakecase, es mas recomendado.
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