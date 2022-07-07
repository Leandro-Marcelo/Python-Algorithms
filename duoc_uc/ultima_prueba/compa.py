import random

# Base de datos
numero_parte=[]
nombre_producto=[]
precio_producto=[]
descripcion_producto=[]

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

def app():
    while True:
        option = menu("Grabar", "Buscar", "Imprimir", "Salir")
        if option == 1:
            print("===> Grabar")
            grabar()
        if option == 2:
            print("===> Buscar")
            buscar()
        if option == 3:
            print("===> Imprimir")
            imprimir()
        if option == 4:
            print("===> Saliendo de la aplicación")
            salir()
            return

def grabar():
    while True:
        letras = "abcdefghijklmnopqrstuvwxyz"
        parte = ""
        for i in range(6):
            numero = random.randint(0,9)
            parte+=str(numero)
        
        numero = random.randint(0,25)
        parte = f'{parte}-{letras[numero].upper()}'

        for i in range(2):
            numero = random.randint(0,9)
            parte+=str(numero)
        
        while True:
            # validar que no pueda ingresar numeros
            nombre = input('Ingrese nombre del producto: ')
            if len(nombre)>=6:
                break
            else:
                print('Numero de caracteres insuficientes, debe contener minimo 6 - Intente Nuevamente')

        while True:
            try:
                precio = float(input('Ingrese precio del producto: '))
                if precio>0:
                    break
                else:
                    print('Precio inválido - Intente Nuevamente')
            except:
                print('Precio inválido - no puede ingresar una letra')

        while True:
            # validar que no pueda ingresar numeros
            descripcion = input('Ingrese descripción del producto del producto: ')
            if len(descripcion)>=20:
                break
            else:
                print('Numero de caracteres insuficientes, debe contener minimo 20 - Intente Nuevamente')

        numero_parte.append(parte)
        nombre_producto.append(nombre)
        precio_producto.append(precio)
        descripcion_producto.append(descripcion)

        print('Producto grabado')
        print(parte)
        print(nombre)
        print(precio)
        print(descripcion)

        break

def buscar():
    while True:
        parte = input('Ingrese número de parte: ')
        if parte in numero_parte:
            print(f'{nombre_producto[numero_parte.index(parte)]} {precio_producto[numero_parte.index(parte)]}')
            print(f'Nombre del producto: {nombre_producto[numero_parte.index(parte)]}')
            print(f'Precio del producto: {precio_producto[numero_parte.index(parte)]}')
            print(f'Descripción del producto: {descripcion_producto[numero_parte.index(parte)]}')
            break
        else:
            print('Número de parte no encontrado')
            break

def imprimir():
    while True:
        for i in range(len(numero_parte)):
            print(f'{numero_parte[i]} {nombre_producto[i]} {precio_producto[i]} {descripcion_producto[i]}')
        break

def salir():
    print('Gracias por utilizar la aplicacion, leandro marcelo version 1.0')

app()
        



