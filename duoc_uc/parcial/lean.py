users_registered = []
email_validated = None

rut = 3000000
edad = -30
gender = ['M', 'F']
gender_flat = True
type_flat = True
email_flat = True
types = ['PREMIUM', 'GOLD', 'SILVER']
suscripciones = []
logged = False

flag = 1

while flag == 1:
    print("1° Registrar Cliente")
    print("2° Subscripcion")
    print("3° Consultar Datos Cliente")
    print("4° Salir")
    try:
        option = int(input("Ingrese una opcion: "))
        if option >= 1 and option <= 4:
            if option == 1:
                while not(4000000 <= rut <= 99999999):
                    rut = int(input("Ingresar rut: "))
                nombre = input("Ingresar nombre: ")
                direccion = input("Ingresar direccion: ")
                comuna = input("Ingresar comuna: ")
                while email_flat:
                    correo = input('ingresa un correo, recuerda que un correo valido debe contener @: ')
                    for i in range(len(correo)):
                        print(correo[i])
                        if correo[i] == '@':
                            email_flat = False
                while not(0 < edad < 110):
                    edad = int(input("Ingresar edad: "))
                while gender_flat:
                    genero = input("Ingresar M (Masculino) o F (Femenino) : ")
                    if len(genero) == 1:
                        if genero in gender:
                            gender_flat = False
                        else:
                            print('El genero ingresado no es ni M ni F, por favor, ingresa M o F dependiendo de su genero')
                    else:
                        print('Debes Ingresar solo una letra y específicando si M (Masculino) o F (Femenino)')
                celular = input("Ingresar celular: ")
                while type_flat:
                    tipo = input(f'Tipos permitidos "PREMIUM", "GOLD", "SILVER", ingresa el tipo: ')
                    if tipo in types:
                        type_flat = False
                    else:
                        print('El tipo ingresado no es valido')
                subscripciones = 'suscrito'
                users_registered.append({'rut': rut, 'nombre': nombre, 'direccion':direccion, 'comuna':comuna, 'correo':correo, 'edad':edad, 'genero':genero, 'celular':celular, 'tipo':tipo, 'subscripciones':subscripciones})
                rut = 3000000
                edad = -30
                gender = ['M', 'F']
                gender_flat = True
                type_flat = True
                email_flat = True
                print(users_registered)
            elif option == 2:
                try:
                    input_rut = int(input('Ingresa un rut: '))
                    for i in range(len(users_registered)):
                        if users_registered[i]['rut'] == input_rut:
                            logged = True
                            fecha = input('Ingresa una fecha: ')
                            suscripciones.append(fecha)
                    if not(logged):
                        print('el rut no se encuentra registrado en el sistema')
                    logged = False
                except:
                    print('El rut ingresado no es un número, por favor ingrese un número')
            elif option == 3:
                try:
                    input_rut = int(input('Ingresa un rut: '))
                    for i in range(len(users_registered)):
                        if users_registered[i]['rut'] == input_rut:
                            rut_2 = users_registered[i]['rut']
                            nombre_2= users_registered[i]['nombre']
                            direccion_2 = users_registered[i]['direccion']
                            comuna_2 = users_registered[i]['comuna']
                            correo_2 = users_registered[i]['correo']
                            edad_2 = users_registered[i]['edad']
                            genero_2 = users_registered[i]['genero']
                            celular_2 = users_registered[i]['celular']
                            tipo_2 = users_registered[i]['tipo']
                            subscripciones_2 = users_registered[i]['subscripciones']
                            logged = True
                            print(f'Datos: \n nombre: {nombre_2} \n rut: {rut_2} \n direccion: {direccion_2}, \n comuna: {comuna_2}, \n correo: {correo_2}, \n edad: {edad_2}, \n genero: {genero_2}, \n celular {celular_2}, \n tipo: {tipo_2}, \n subscripciones: {subscripciones_2}')
                    if not(logged):
                        print('el rut del cual quiere obtener los datos, no se encuentra registrado')
                    logged = False
                except:
                    print('El rut ingresado no es un número, por favor ingrese un número')
            elif option == 4:
                break
        else:
            print("opción ingresada no valida, las opciones son las siguientes: ")
    except:
        print(f'Option ingresada no valida, por favor ingrese algunas de las opciones mostradas')



