# vamos a trabajar loops o bucles

'''number = 0
while number < 5: # La sentencia se ejecuta hasta que se cumpla o sea diferente y se acaba el proceso
    print('Numero es:', number)
    number+=1
'''

# Controlando la exepcion para mostrar un resultado final
number = 0
while number < 6:
    print('Numero es:', number)
    number+=1
else:
    print('Numero final:', number)

# Parar el ciclo o romperlo
number = 0
while number < 5: #Aca controlamos cuando acabar el ciclo con la condicion if y el break
    print('Numero es:', number)
    number+=1
    if number == 3:
        break

# Uso del bucle for, este usado para iterar en listas, tupas, diccionario o conjuntos de cadenas

''' for element in range:
        code to execute
'''

numeros = [0,1,2,3,4,5]
for numero in numeros:
    print(numero)

language = 'Python'
for i in range(len(language)):
    print(language[i])

# Bucle con far para datos clave valor

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

for key, value in persona.items():
    print(key, ':', value)

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# Tambien se puede parar o romper los ciclos cuando se cumple los condicionales

for numero in numeros:
    print(numero)
    if numero==3:
        break
    
for num in numeros:
    print(num)
    if num == 3:
        continue
    print('Siguiente numero sera: ', num + 1) if num != 5 else print("Acabo el ciclo") # Modo Corto de hacer condicional
print('Final del for')

# Se puede mostrar o ejecutar comandos cuando aca un for, siendo parte del mismo proceso de for con else

for number in range(11):
    print(number)
else:
    print('El bucle paro en:', number)


# Ejercicion simples
a = '#'
for i in range(7):
    print(a)
    a = a + '#'

b = ""
n = 8
for i in range(n):
    if i < 1 :
        for j in range(n):
            b = b + " X"
    print(b)


for i in range(11):
    r = i * i
    print(i,'X',i,'=',r)

# Mostrar numeros pares con while
lista = list(range(101))
h = 0
while h <= 100:
    r = lista[h] % 2
    if r == 0:
        print(h)
    h +=1

# Mostrar numeros impares con while
lista = list(range(101))
h = 0
while h <= 100:
    r = lista[h] % 2
    if r != 0:
        print(h)
    h +=1