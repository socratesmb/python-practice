# Condicionales

# Trabajaremos con if, else, elif

a = 2
if a >= 0: # If simple si cumple pasa si no, no muestra nada
    print('correcto es un numero positivo')
    
a = -3
if a >= 0: # If con else, evalua las 2 condiciones si cumple muestra si no muestra por defecto otro resultado
    print('Es positivo')
else:
    print('Es negativo')

b = 0
if b > 0: # If con elif y else, evaluando y teniendo encuenta todos los posibles datos.
    print('Es positivo')
elif b < 0:
    print('Es negativo')
else:
    print('Es cero')

# Se puede reducir el condicional 
a = 3
print('A is positive') if a > 0 else print('A is negative')

# Condicionales anidados

a = -8
if a > 0:
    if a % 2 == 0: # Doble if o un if dentro de otro if con else anidado
        print('Es positivo y entero')
    else:
        print('Es un numero positivo')
elif a == 0:
    print('Es cero')
else:
    print('Es negativo')

# Condicionales if con operadores ligicos

a = 3
if a > 0 and a % 2 == 0: # Condicional if else mas y, and &
        print('Es entero par positivo')
elif a > 0 and a % 2 !=  0:
     print('Es entero positivo')
elif a == 0:
    print('Es cero')
else:
    print('Es negativo')


user = 'Socrates'
access_level = 2
if user == 'admin' or access_level >= 3: # Condicional if mas o, or ||
        print('Acceso concedido!')
else:
    print('Acceso denegado!')
