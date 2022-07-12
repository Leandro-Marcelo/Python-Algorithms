""" Datos de los pasajeros """
ruts=[]
nombres=[]
telefonos=[]
bancos=[]
""" Asientos de los pasajeros """
asientos_ocupados = []

""" app """
asientos = list(range(1,43))
asiento_normal = 78900
asiento_vip = 240000

""" validacion de elementos que no puede contener un nombre """
validacion_nombre = ["1234567890!@#$%^&*()_+=-"]
flag = True

def menu(*args):
    while True:
        i = 1
        for arg in args:
            print(i, '.-',arg)
            i+=1
        try:
            opc=int(input('Ingrese Opción: '))
            if opc>0 and opc<i:
                return opc
            else:
                print('Opcion Incorrecta - Intente Nuevamente')
        except:
            print('Opción Inválida - Intente Nuevamente')

def asientos_disponibles():
    print("asientos")
    print(asientos)
    print("ruts")
    print(ruts)
    print("nombres")
    print(nombres)
    print("telefonos")
    print(telefonos)
    print("bancos")
    print(bancos)
    print("asientos_ocupados")
    print(asientos_ocupados)

def buy_seat():
    try:
        rut = int(input('Ingrese su rut: '))
        telefono = int(input('Ingrese su telefono: '))
    except:
        print("Opción Inválida - Intente Nuevamente")
    while flag:
        nombre = input('ingresa su nombre: ')
        for letra in range(len(nombre)):
            if nombre[letra] in validacion_nombre:
                print("El nombre no puede contener este caracter", nombre[letra])
                flag = True
                break
            else:
                flag = False
                
    while True:
        try:
            banco = int(input("¿Es usuario de 'bancoDuoc'? (Si = 1) (No = 0): "))
            if banco == 1 or banco == 0:
                break
            else:
                print("Ingrese un valor válido para continuar")
        except:
            print('Opción Inválida - Intente Nuevamente')
    print('Asientos Disponibles')
    print(asientos)
    while True:
        try:
            asiento = int(input('Ingrese asiento: '))
            if asiento in asientos:
                if banco == 1 and asiento in range(0,31):
                    print("El precio por el asiento normal es: ", asiento_normal)
                    print("Pero por ser usuario de 'bancoDuoc' le aplicamos el descuento del 15% quedando como total: ", asiento_normal - ((asiento_normal*15)/100))
                if banco == 1 and asiento in range(31,43):
                    print("El precio por el asiento vip es: ", asiento_vip)
                    print("Pero por ser usuario de 'bancoDuoc' le aplicamos el descuento del 15% quedando como total: ", asiento_vip - ((asiento_vip*15)/100))
                if banco == 0 and asiento in range(0,31):
                    print("El total por el asiento normal fue de: ", asiento_normal)
                if banco == 0 and asiento in range(31,43):
                    print("El total por el asiento vip fue de: ", asiento_vip)
                break
            else:
                print('Asiento no disponible')
        except:
            print('Opción Inválida - Intente Nuevamente')
    ruts.append(rut)
    nombres.append(nombre)
    telefonos.append(telefono)
    bancos.append(banco)
    asientos_ocupados.append(asiento)
    asientos[asiento-1] = "X"

def cancelar_pasaje():
    print("Para cancelar el pasaje, tendrá que ingresar su rut y numero de asiento")
    while True:
        try:
            rut = int(input('Ingrese su rut: '))
            asiento = int(input('Ingrese su asiento: '))
        except:
            print("Opción Inválida - Intente Nuevamente")
        if asiento in asientos_ocupados:
            indice = asientos_ocupados.index(asiento)
            if rut == ruts[indice]:
                ruts.pop(indice)
                nombres.pop(indice)
                telefonos.pop(indice)
                bancos.pop(indice)
                asientos_ocupados.pop(indice)
                asientos[asiento-1] = asiento
                print("Pasaje cancelado")
                break
            else:
                print("El rut ingresado no coincide con el rut del pasajero de ese asiento")
        else:
            print("El asiento no se encuentra ocupado ó no existe")

def modificar_datos():
    while True:
        try:
            rut = int(input('Ingrese su rut: '))
            asiento = int(input('Ingrese su asiento: '))
        except:
            print("Opción Inválida - Intente Nuevamente")
        if asiento in asientos_ocupados:
            indice = asientos_ocupados.index(asiento)
            if rut == ruts[indice]:
                while True:
                    print("Qué dato quieres modificar:")
                    option = menu(f'Modificar nombre {nombres[indice]}', f'Modificar telefono {telefonos[indice]}', "salir")
                    if option == 1:
                        nombres[indice] = input('Ingrese nuevo nombre: ')
                        print("Dato modificado")
                    elif option == 2:
                        telefonos[indice] = input('Ingrese nuevo telefono: ')
                        print("Dato modificado")
                    elif option == 3:
                        break
            else:
                print("El rut ingresado no coincide con el rut del pasajero de ese asiento")
            break
        else:
            print("El asiento no se encuentra ocupado ó no existe")

def app():
    while True:
        option = menu("Ver asientos disponibles", "Comprar asiento", "Anular vuelo", "Modificar datos de pasajero", "Salir")
        if option == 1:
            asientos_disponibles()
        if option == 2:
            buy_seat()
        if option == 3:
            cancelar_pasaje()
        if option == 4:
            modificar_datos()
        if option == 5:
            print("===> Saliendo de la aplicación")
            return

app()