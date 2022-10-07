## Trabajaremos con diccionarios
# Son colecciones de datos no ordenados y modificables emparajerados por clave:valor

diccionario = {}

dicc = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(type(dicc))
print(dicc)

# Construccion de un diccionaro mas grande

persona = {
    'first_name':'Socrates',
    'last_name':'Martinez',
    'age':25,
    'country':'Colombia',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(type(persona))
print(len(persona))
print(persona)

# Acceso a los datos del diccionario

print(dicc['key3']) # Acceso simple
print(persona['first_name']) # Acceso simple
print(persona['skills'][2]) # Acceso un indice concreto dentro del set 

# Obtener los datos completos

print(persona.get('skills')) # Con el get se realiza la consulta en el diccionario, en caso de no encontrar la clave,
print(persona.get('address')) # devuelve none, pero no generar error o problema de datos al no existir
print(persona.get('state'))

# Adicionando o modificando elementos a un diccionario

persona['first_name'] = 'Juan' # Modificamos el nombre
print(persona)

persona['job_tittle'] = 'Ingeniero de Sistemas' # Agregamos una clave valor nueva al diccionario, se agrega al final
print(persona)

persona['skills'].append('HTML5') # Agregando un nuevo valor dentro de una clave con listas
print(persona)

# Comprobar datos en el diccionario
print('socrates' in persona) # No encuentra porque esta buscando un valor
print('first_name' in persona) # Encuentra porque se busca la clave, la cual existe

# Eliminacion de claves valor en el diccionario

dicc.pop('key1') #Borra la clave indicada
print(dicc)
dicc.popitem() # Elimina la ultima clave
print(dicc)

dicc['key3'] = 'value3'
dicc['key4'] = 'value4'
print(dicc)

del dicc['key3'] # Podemos borrar de esta manera la clave exacta
print(dicc)

# Cambio de diccionario a una lista de elementos

print(dicc.items()) # La funcion items() cambia el dicts por una tuple

# Borrar el diccionario y duplicado de elementos

# print(dicc.clear()) # Limpia el diccionario pero no lo borra

# del dicc # Aca borramos por completo el diccionario
# print(dicc) # Da error porque no existe

copia_dicc = dicc.copy()
print(copia_dicc)

# Otras fucciones
print('-----------')
print(dicc.items()) # Retorna las clave valor del diccionario
print(dicc.keys()) # Retorna solo las claves del diccionario
print(dicc.values()) # Retorna solo los valores del diccionario