# Trabajaremos Listas #

from numpy import empty


lista = list() #Lista instaciada pero vacia

lista2 = ['casa', 'carro', 'moto', 'parque'] # Lista creada con variables
print(lista2)
print(len(lista2))

lista3 = ['socrates', 25, True, {'pais': 'colombia', 'departamento': 'antioquia', 'ciudad':'medellin'}] # Lista con multiples datos
print(lista3[2]) #Mostrar lista en posicion especifica
print(lista3[len(lista3)-1]) #Mostrar la ultima posicion de la lista
print(lista3[-1]) # Lo mismo que arriba, pero otra notacion

# Desempaquetado de listas
lista4 = ['mora', 'fresa', 'uva', 'naranja', 'mango', 'lemon']
p1_fruta, p2_fruta, p3_fruta, *resto = lista4
print(p1_fruta)
print(p2_fruta)
print(p3_fruta)
print(resto)
print(lista4[0:3])
print(lista4[1:])
print(lista4[::2]) # Muestra los datos cada n iteraciones, partiendo desde la posicion 0

# Desenpaquetado de listas con variable * acumuladora
lista5 = [1,2,3,4,5,6,7,8,9,10]
firt, second, third, *rest, tenth = lista5
print(firt)
print(second)
print(third)
print(rest)
print(tenth)

print(lista4 + lista5)

# Modificaciones o mutacion de listas
lista4 = ['mora', 'fresa', 'uva', 'naranja', 'mango', 'limon']
lista4[0] = 'lulo' # Mutamos o modificamos la posicion 0 de la lista
lista4[-1] = 'tomate' # Modificamos la ultima posicion de la lista
print(lista4)

# Validacion de datos en listas
existe1 = 'mora' in lista4;
print(existe1)
existe2 = 'lulo' in lista4;
print(existe2)

# Agregacion de elementos nuevos a la lista
lista4.append('manzana') # Con append la insercion se genera al final
print(lista4)

lista4.insert(2, 'limon') # Con insert agrega en el indice n y la variable que deseamos
print(lista4)

lista4.remove('tomate') # Podemos eliminar directo de la lista el valor que desamos
print(lista4) # Al eliminar el valor elimina es el primer encontrado

lista4.pop() # Elimina el ultimo indice, pero se puede agregar el n indice que deseemos quitar, este valor es guardable en una variable
print(lista4)

# Eliminar o limpiar la lista
print(lista2) # Mostramos la lista normal
lista2.clear() # Borramos o limpiamos la lista
print(lista2)

# Copia de listas
lista_copia = lista3 # De esta manera tenemos la copia de la lista, pero esta esta referencia a la lista original, si se cambia algo en la lista original la lista instaciada tambien cambiara
print(lista_copia)

lista_copia2 = lista3.copy() # De este modo es una copia inmutable y no importa las modificaciones de la lista original, nuestra copia no se modificara
print(lista_copia2)


# Union de listas en una misma lista, sin la instancia de +
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
print(list1)

# Invertir una lista
print(lista3)
lista3.reverse() # Re ordena los datos en el orden contrario
print(lista3)

# Ordenamiento de lista
lista4.sort() # El ordemiento de las listas se realiza en orden ASCII o numerico, esto modifica las listas
print(lista4)

print(sorted(lista4, reverse=True)) # Con sorted podemos reordenas la lista, sin modificar la misma lista, es un vista nada mas