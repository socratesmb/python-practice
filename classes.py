# Clases

class Persona:
    def __init__(self, name, surname):        
        self.name = name
        self.surname = surname
        

my_person = Persona('Socrates', 'Martinez')

print(my_person.name)
print(f"{my_person.name} {my_person.surname}")

#Tambien se puede concatenar variables dentro de un clase

class Animal:
    def __init__(self, name, lastname):
        self.full_name = f'{name} {lastname}'
        
mi_perrito = Animal('Aura', 'Martinez')
print(mi_perrito.full_name)

# Se puede agregar funciones dentro de las clases

class Persona1:
    def __init__(self, firsname, lastname, age, country, city):
        self.firsname = firsname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    def Datos_Persona(self):
        return f'{self.firsname} {self.lastname} tiene: {self.age} años, nacio en: {self.country} y vive en {self.city}'
    
user = Persona1('Socrates', 'Martinez', 25, 'Colombia', 'Medellin')
print(user.firsname)
print(user.Datos_Persona())

# Como en las funciones se puede tener las clases con variables inicializadas
# Tambien se puede modificar valores con una funccion para agregar
class Persona2:
    def __init__(self, user, email, skill = 'HTML'):
        self.user = user # Variables Publicas
        self.email = email
        self.__skills = [skill] # Variable privada
    def Datos_Persona(self):
        return f'{self.user} correo: {self.email}, con habilidades en {self.__skills}'
    def Agregar_Skills(self, skill):
        self.__skills.append(skill)
        
user2 = Persona2('socratesmb', 'sberrio634@gmail.com')
print(user2.email)
print(user2.Datos_Persona())

user2.Agregar_Skills('JavaScrip')
user2.Agregar_Skills('NodeJS')
user2.Agregar_Skills('Python')
print(user2.Datos_Persona())