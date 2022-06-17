codigo=[]
mascota=[]
while True:
    print('1.- Ingreso Mascota')
    print('2.- Modifica Mascota')
    print('3.- Elimina Mascota')
    print('4.- Lista Mascotas')
    print('5.- Salir')
    try:
        opcion=int(input('Ingrese Opción: '))
        if opcion==1:
            codigo.append(input('Ingrese Código de la Mascota: '))
            mascota.append(input('Ingrese Nombre de la Mascota: '))
        elif opcion==2:
            cod=input('Ingrese Código de la Mascota a Modificar: ')
            indice=codigo.index(cod)
            print('El Nombre de la Mascota es ',mascota[indice])
            opc=input('Desea cambiar el nombre si/no: ')
            if opc.upper()=='SI':
                mascota[indice]=input('Ingrese Nuevo Nombre: ')
        elif opcion==3:
            cod=input('Ingrese Código de la Mascota a Eliminar: ')
            indice=codigo.index(cod)
            print('El Nombre de la Mascota es ',mascota[indice])
            opc=input('Desea eleminar a esta pobre mascota si/no: ')
            if opc.upper()=='SI':
                mascota.pop(indice)
                codigo.pop(indice)
        elif opcion==4:
            print('Código       Nombre')
            print('====================')
            for i in range(len(codigo)):
                print(codigo[i],'     ',mascota[i])
        elif opcion==5:
            break
        else:
            print('La opción de estar entre 1 a 5')
    except:
        print('Opción Incorrecta - Intente Nuevamente')

