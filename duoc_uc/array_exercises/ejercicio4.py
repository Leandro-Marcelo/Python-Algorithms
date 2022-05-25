nombres=[]
for _ in range(3):
    nombres.append(input('Ingrese un nombre: '))
mayor=nombres[0]
for i in nombres:
    if len(i)>=len(mayor):
        mayor=i
print ('la palabra con mayor cantidad de caracteres es',mayor)