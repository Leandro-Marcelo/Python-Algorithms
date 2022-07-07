ruts=[]
nombres=[]
apellidos_paternos=[]
edades=[]
estados_civiles=[]
generos=[]
fechas_afiliaciones=[]

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

def grabar():

    while True:
        try:
            rut = int(input('Ingrese su rut sin digito verificador: '))
            if(rut<4000000 or rut>99999999):
                print("El rut ingresado no es valido, por favor intentelo nuevamente.")
            else:
                print('rut correcto')
                break
        except:
            print('No ingrese caracteres, recuerde que un rut solamente puede ser numerico')

    while True:
        try:
            edad = int(input('Ingrese su edad: '))
            if edad <= 18:
                print("La edad tiene que ser mayor a 18.")
            else:
                print("edad correcta")
                break
        except:
            print('Opción Inválida - Intente Nuevamente')

    while True:
        estado_civil = input("Ingrese su estado civil, C para casado, S para soltero y V para viudo: ")
        estado_civil = estado_civil.upper()
        if (estado_civil == "C" or estado_civil == "S" or estado_civil == "V"):
            print('estado civil correcto')
            break
        else:
            print("Dato ingresado incorrecto, vuelva a intentarlo.")

    while True:
        genero = input("Ingrese su genero, M para masculino y F para femenino: ")
        genero = genero.upper()
        if (genero == "M" or genero == "F"):
            print('genero correcto')
            break
        else:
            print("Dato ingresado incorrecto, vuelva a intentarlo.")

    nombre = input('Ingrese su primer nombre: ')
    apellido_paterno = input('Ingrese su apellido paterno: ')
    fecha_afiliacion = input('Ingrese la fecha de afiliacion: ')

    ruts.append(rut)
    nombres.append(nombre)
    apellidos_paternos.append(apellido_paterno)
    edades.append(edad)
    estados_civiles.append(estado_civil)
    generos.append(genero)
    fechas_afiliaciones.append(fecha_afiliacion)

def buscar():
    while True:
        try:
            rut = int(input('Ingrese el rut, sin digito verificador, que quiere buscar: '))
            if rut in ruts:
                break
            else:
                print('El rut no existe en la base de datos')
        except:
            print("Dato ingresado incorrecto, vuelva a intentarlo.")
    indice = ruts.index(rut)
    print(f'Los datos son: \n {ruts[indice]} {nombres[indice]} {apellidos_paternos[indice]} {edades[indice]} {estados_civiles[indice]} {generos[indice]} {fechas_afiliaciones[indice]}')

def imprimir():
    while True:
        try:
            rut = int(input('Ingrese el rut, sin digito verificador: '))
            tipo_certificado = int(input('Ingrese que tipo de certificado quiere, el de 1000 o el de 1500: '))
            if tipo_certificado == 1000 or tipo_certificado == 1500:
                if rut in ruts:
                    break
                else:
                    print('El rut no existe en la base de datos')
            else:
                print('El tipo de certificado no existe en la base de datos')
        except:
            print("Dato ingresado incorrecto, vuelva a intentarlo.")
    indice = ruts.index(rut)
    
    print(f'--------------------- Imprimiendo certificado de afiliacion de {tipo_certificado} ---------------------')
    print(f'Datos de la persona: ')
    print(f'\n rut: {ruts[indice]} \n nombre: {nombres[indice]} \n apellido: {apellidos_paternos[indice]} \n edad: {edades[indice]} \n estado civil: {estados_civiles[indice]} \n genero: {generos[indice]} \n fecha afiliacion: {fechas_afiliaciones[indice]}')


def salir():
    print('Gracias por utilizar la aplicacion de VIDA Y SALUD, leandro marcelo version 1.0')

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

app()
