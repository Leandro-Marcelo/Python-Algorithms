user1, user2, user3, password1, password2, password3 = None, None, None, None, None, None

users_registered = []
email_validated = None

flag = 1

while flag == 1:
    print("1° Iniciar sesión")
    print("2° Registrar Usuario")
    print("3° Salir")
    try:
        option = int(input("Ingrese una opcion: "))
        if option >= 1 and option <= 3:
            if option == 2:
                print("\nIngrese su usuario y contraseña")
                user = input("Ingresar usuario: ")
                password = input("Ingresar contraseña: ")
                if (not(user1)):
                    user1 = user
                    password1 = password
                    users_registered.append({'user': user1, 'password': password1})
                elif not(user2):
                    user2 = user
                    password2 = password
                    users_registered.append({'user': user2, 'password': password2})
                elif not(user3):
                    user3 = user
                    password3 = password
                    users_registered.append({'user': user3, 'password': password3})
                else:
                    print('No hay capacidad para registrar mas usuarios')
            elif option == 1:
                print("\nIngrese su usuario y contraseña")
                user = input("Ingresar usuario: ")
                password = input("Ingresar contraseña: ")
                for i in range(len(users_registered)):
                    if users_registered[i]['user'] == user and users_registered[i]['password'] == password:
                        print('1° Realizar llamada')
                        print('2° Enviar Correo')
                        print('3° Cerrar sesión')
                        try:
                            option2 = int(input("Ingrese una opcion: "))
                            if option2 >= 1 and option2 <= 3:
                                if option2 == 1:
                                    numTelefono = input(f'ingresa el numero de telefono: ')
                                    if numTelefono[0] == '9':
                                        if len(numTelefono) == 9:
                                            print('Se realiza la llamada')
                                        else:
                                            print('el numero ingresado despues del 9 tiene mas de 8 digitos')
                                    else:
                                        print('El numero ingresado no empieza con 9')
                                elif option2 == 2:
                                    input_correo = input('ingresa un correo: ')
                                    for i in range(len(input_correo)):
                                        if input_correo[i] == '@':
                                            email_validated = True
                                    if email_validated:
                                        message = input('ingresa el mensaje')
                                        correo = input_correo
                                        print('correo guardado')
                                        print('mensaje guardado')
                                    else:
                                        print('El correo ingresado no posee un @')
                                else:
                                    print('volviendo al menu principal')
                        except:
                            print("2° Solo se permite las opciones 1, 2 y 3")
                    else:
                        print('el usuario y contraseña son incorrectos')
            # vuelve al menu principal, no es que cierra el programa
            elif option == 3:
                break
        else:
            print('Solo se permite las opciones 1, 2 y 3')
    except:
        print("Salto el except")



