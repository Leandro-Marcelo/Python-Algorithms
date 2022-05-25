nombres=[]
while True:
    try:
        opc=input('Desea ingresar un nombre? escriba SI o NO: ')
        if opc.upper() == 'SI':
          nombres.append(input('Ingrese nombre: '))
        else:
            break  
    except:
        print('Opcion incorrecta - Ingrese SI o NO')
menor=nombres[0]
for i in nombres:
    if len(i)<=len(menor):
        menor=i
nombres.remove(menor)
print ('la palabra eliminada es: ',menor)
print ('La lista de nombres ingresados es: ',nombres)