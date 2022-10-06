# Vamos a construir tuplas 

# Estas pueden ser diferentes tipos de datos, estos son inmutables y organizados
tupla1 = tuple() # Se puede instaciar con la funcion especifica
tupla2 = () # Pero se puede hacer asi de sencilla

tupla1 = ('rojo', 'verde', 'azul', 'morado', 'verde')
print(tupla1)
print(type(tupla1))
# Las tuplas con colecciones de datos inmutables, osea no podemos agregar, quitar o modificar datos dentro de esta misma.

print(tupla1[1]) # Se pueden llamar los indices igual que las listas
print(tupla1[-1])

# Rebanar o slice de las tuplas
print(tupla1[0:3])
print(tupla1[::2])

# Conteo e index data
print(tupla1.count('verde'))
print(tupla1.index('morado'))

# Se puede pasar las tuplas a listas
lista1 = list(tupla1)
print(lista1)

# Tambien se pueden unir tuplas
tupla3 = (1,2,3,4,5,6,7,8,9,10,11)

suma_tupla = tupla1 + tupla3
print(suma_tupla)

# Ahora vamos a eliminar tuplas
del tupla3
# print(tupla3) # No la va a mostrar, porque la lista se borra por completo

# Comprobacion de elementos dentro de la tupla

print('verde' in tupla1) # La consulta se realiza con la variable in
print('verde' in tupla2)