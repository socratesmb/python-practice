# Trabajaremos listas de comprension

#[i for i in interacion if exprecion]

import math
texto = 'Python'
txt = list(texto)
print(type(txt))
print(txt)

txt2 = [i for i in texto]
print(type(txt2))
print(txt2)

# Generacion de listas
num = [i for i in range(21)]
print(num)

# Se puede agregar operaciones numericas en las listas
cuadrado = [i * i for i in range(21)]
print(cuadrado)

# Es posible crear tuplas tambien
tuplas_num = [(i, i+i) for i in range(21)]
print(tuplas_num)

# Se puede agregar condicionales a las listas de comprension
par_numero = [i for i in range(21) if i % 2 == 0]
inpar_numero = [i for i in range(21) if i % 2 != 0]
print(par_numero)  # Se crea una lista y se condiciona solo a numeros pares
print(inpar_numero)  # Impares

# Lista de positivos o negativos
p_num = [i for i in range(-7, 7) if i >= 0]
n_num = [i for i in range(-7, 7) if i <= 0]
print(p_num)
print(n_num)

# Tambien se pueden agregar funciones, que operen y al mismo tiempo usar modulos 'math'

def cubo(i):
    return math.pow(i, 3)

lis_cubo = [cubo(i) for i in range(21)]
print(lis_cubo)

# funcion lambda, es pequeña anonima y sin nombre

def sum_num(a, b):
    return a + b
print(sum_num(9,4)) # Una funcion simple

suma_num = lambda a, b: a+b # Misma funcion con lambda
print(suma_num(9,2))

print((lambda a,b: a*b)(9,2)) # Se puede autoincovar y hacer mas simple u optimizada
print((lambda a : a ** 2)(4)) # Calculo cuadrado con lambda
print((lambda a : a ** 3)(4)) # Calculo cubo con lambda

f = lambda a,b,c : a**2 - 3 *b + 4 * c
print(f(5,5,3)) # Funcion
print((lambda a,b,c : a**2 - 3 *b + 4 * c)(5,5,3)) # Lo mismo pero mas simple