# Manejo de exepciones y errores

n1, n2 = 12, 34
print(n1 +n2) 

if n1 > 20:
    print('entro')
else:
    print('no entro')

# Uso de try, except para controlar codigo y no romper la ejecucion del codigo
n3 = '2'
try:
    print(n1+n3)
    print('Ejecuta sin error')
except:
    print('Error en codigo')
else:
    print('Ejecuta')
finally:
    print('Ejecuta siempre')
