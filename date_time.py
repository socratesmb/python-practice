# Trabajaremos el modulo datetime
import datetime

print(dir(datetime))

from datetime import datetime as dt

now = dt.now()
año = now.year
mes = now.month
dia = now.day
hora = now.hour
minuto = now.minute
segundo = now.second

print(now)
print(año)
print(mes)
print(dia)
print(hora)
print(minuto)
print(segundo)

timestam = now.timestamp() # Marca de tiempo Unix
print(timestam)

# Formateo de fecha y hora con stfftime
t = now.strftime("%H:%M:%S")
print(t)
t2 = now.strftime("%d/%m/%Y, %H:%M:%S")
print(t2)

# 