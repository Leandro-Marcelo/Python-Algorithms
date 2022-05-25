nombres=[]
apellidos=[]
for _ in range(3):
    nombres.append(input('Ingrese nombre: '))
    apellidos.append(input('Ingrese apellido: '))
print('Nombre       Apellido')
print('====================')
for i in range(len(nombres)):
    print(nombres[i],'     ',apellidos[i])