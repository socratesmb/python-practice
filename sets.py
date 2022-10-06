# Conjuntos

# Creacion de conjuntos o set de 2 formas distintas
conjunto = set()
conjunto2 = {}

# Estructuras de set "conjunto" o dict "diccionario"
print(type(conjunto))
print(type(conjunto2))

# Conjunto simple con agregacion simple
conjunto1 = {'banana', 'orange', 'mango', 'lemon'}
print(len(conjunto1))
conjunto1.add('apple')
print(conjunto1)

# Agregar elementos en conjunto, no puede agregar datos repetidos dentro de los conjuntos
conjunto1.update(['tomato', 'potato', 'cabbage','onion', 'carrot']) #La insercion de datos es en el indice 0 y no es una estructura ordenada
print(conjunto1)

# Ahora vamos a eliminar un elemento del conjunto
conjunto1.remove('carrot')
print(conjunto1)

# Comprabacion de datos en conjuntos
print('banana' in conjunto1)
print('carrot' in conjunto1)

# Eliminacion de un datos en la lista de modo random con pop
value_remove = conjunto1.pop()
print(value_remove)
print(conjunto1)

# Borrar articulos de los conjuntos de listas
fruits = {'b', 'o', 'm', 'l'}
fruits.clear() # Con esto dejamos el conjunto existiendo pero vacio o empty
print(fruits)

# del fruits
# print(fruits) # Muestra error porque el conjunto no existe.

# Union de conjuntos
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) # En este conjunto se unen los st1 y st2
print(st1)
print(st2)
print(st3)

# Diferencia de conjuntos
print(st3.difference(st1)) # Aca estamos mostrando la diferencia de los datos que no son iguales

# Actualizacion de conjuntos
st1.update(st2) # Esto actualiza el conjunto insertando los valores nuevos en el conjunto ya existente
print(st1) 

# Interseccion de conjuntos, de igual manera estos datos son guardables en variables
print(st3.intersection(st2)) # Esto nos muestra los datos que son iguales en los conjuntos, o que estan en los 2 conjuntos al mismo tiempo

# Comprobacion de subconjuntos "issubset" y superconjuntos "ussuperset"
print('----------')
print(st1.issubset(st3)) # St1 es un conjunto dentro de st3
print(st3.issuperset(st1)) # St3 es el super conjunto de st1 ya que todos los valores de st1 estan en st3