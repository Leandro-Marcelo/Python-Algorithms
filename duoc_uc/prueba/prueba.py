while True:
    rut=[]
    nombre = []
    direccion = []
    comuna = []
    correo = []
    edad = []
    genero = []
    celular = []
    tipo_suscripcion = []
    suscripcion = []
    verificador = 0
    while True:
        print("Juan Maestro App: ")
        print("1. Registrar Cliente")
        print("2. Consultar Datos Cliente")
        print("3. Suscripcion")
        print("4. Salir")
        contador = 0
        try:
            opcion = int(input())            
            if(opcion == 1):
                while (verificador == 0):
                    while (contador == 0):
                        try:
                            rut_nuevo = int(input("Ingrese su rut sin digito verificador ni guiones, o presione 0 para salir:\n"))
                            if(rut_nuevo == 0):
                                contador = 1
                                a = int(1)
                                a =+ "a"
                            else:
                                if(rut_nuevo<4000000 or rut_nuevo>99999999):
                                    print("El rut ingresado no es valido, por favor intentelo nuevamente.")
                                else:
                                    rut.append(rut_nuevo)
                                    verificador = 1
                                    contador = 1
                        except:
                            if(rut_nuevo != 0):
                                print("El rut ingresado no es valido, por favor intentelo nuevamente.")
                    if(verificador == 1):
                        nombre_nuevo = input("Por favor ingrese su nombre:\n")
                        nombre.append(nombre_nuevo)
                        direccion_nueva=input("Ingrese su direccion por favor:\n")
                        direccion.append(direccion_nueva)
                        comuna_nueva=input("Ingrese su comuna:\n")
                        comuna.append(comuna_nueva)
                        verificador = 0
                    else:
                        verificador = 1
                    while (verificador==0):
                        correo_nuevo= input("Ingrese su correo:\n")
                        if (len(correo_nuevo) > 1):
                            correo.append(correo_nuevo)
                            verificador=1
                            contador = 0
                        else:
                            print("El correo ingresado no es valido, por favor intentelo nuevamente")
                    verificador = 0
                    if(contador == 1):
                        verificador = 1
                    while (verificador == 0):
                        try:
                            edad_nueva=int(input("Ingrese su edad:\n"))
                            if(edad_nueva<0 or edad_nueva>110):
                                print("La edad ingresada no es correcta, por favor ingrese su edad nuevamente.")
                            else:
                                verificador = 1
                                edad.append(edad_nueva)
                        except:
                            print("La edad ingresada no es correcta, ingrese nuevamente")
                    verificador = 0
                    if(contador == 1):
                        verificador = 1
                    while(verificador==0):
                        genero_nuevo = input("Ingrese su genero:\nM para masculino y F para femenino\n")
                        genero_nuevo = genero_nuevo.upper()
                        if (genero_nuevo == "M" or genero_nuevo == "F"):
                            genero.append(genero_nuevo)
                            verificador = 1
                        else:
                            print("El genero ingresado no es correcto, intentelo nuevamente.")
                    verificador = 0
                    if(contador == 1):
                        verificador = 1                    
                    while (verificador == 0):
                        try:
                            celular_nuevo=int(input("Ingrese su numero de celular despues de 9:\n"))
                            if(celular_nuevo<11111111 or celular_nuevo>99999999):
                                print("El celular ingresado no es correcto, por favor ingrese su celular nuevamente.")
                            else:
                                verificador = 1
                                celular.append(celular_nuevo)
                        except:
                            print("El celular ingresado no es correcto, por favor ingrese su celular nuevamente.") 
                    verificador = 0
                    if(contador == 1):
                        verificador = 1                                      
                    while(verificador==0):
                        tipo_suscripcon_nuevo = input("Ingrese su tipo de suscripcion:\nS para Silver, P para Premium y G para gold\n")
                        tipo_suscripcon_nuevo = tipo_suscripcon_nuevo.upper()
                        if (tipo_suscripcon_nuevo == "S" or tipo_suscripcon_nuevo == "P" or tipo_suscripcon_nuevo == "G"):
                            tipo_suscripcion.append(tipo_suscripcon_nuevo)
                            verificador = 1
                        else:
                            print("El tipo de suscripcion ingresado no es correcto, por favor ingrese nuevamente.") 
                    if(contador != 1):             
                        print("Ususario ingresado correctamente!:)\n")
                    suscripcion.append([])
                verificador = 0
                opcion = 0
            if (opcion == 2):
                while (verificador==0):
                    ayuda = 0
                    try: 
                        buscar_rut = int(input("Ingrese rut a buscar, o presione 0 para salir:\n"))
                        if (buscar_rut != 0):
                            indice = rut.index(buscar_rut)
                            print(f"Resultados de rut: {rut[indice]}")
                            print(f"Nombre: {nombre[indice]}")
                            print(f"Direccion: {direccion[indice]}")
                            print(f"Comuna: {comuna[indice]}")
                            print(f"Correo: {correo[indice]}")
                            print(f"Edad: {edad[indice]}")
                            print(f"Genero: {genero[indice]}")
                            print(f"Celular: {celular[indice]}")
                            print(f"Tipo de Suscripcion: {tipo_suscripcion[indice]}\n")
                            verificador = 1
                        if(buscar_rut == 0):
                            contador = 1
                            a = int(1)
                            a =+ "a"  
                            ayuda = 1                      
                    except:  
                        if(buscar_rut != 0):
                            print("Cliente no registrado, o datos ingresados invalidos, por favor intente nuevamentee\n")
                        else:
                            verificador = 1
                verificador=0 
            if (opcion == 3):
                while (verificador == 0):
                    try:
                        buscar_rut2 = int(input("Ingrese rut a buscar o ingrese 0 para salir:\n"))
                        if(buscar_rut2!=1):
                            indice = rut.index(buscar_rut2) 
                            fecha = input("Ingrese la fecha:\n")
                            suscripcion.append(fecha)
                            print("Fecha ingresada correctamente!\n")
                            verificador = 1
                        if(buscar_rut2 == 0):
                            contador = 1
                            a = int(1)
                            a =+ "a"
                            verificador = 1
                    except:
                        if(buscar_rut2 != 0):
                            print("El rut ingresado no se encuentra registrado o no es valido, por favor intentelo nuevamente\n")
                        else:
                            verificador = 1
            if(opcion==4):
                print("Gracias por suscribirse a la app de Juan Maestro! :)")
                break
        except:
            if(contador == 0):
                print("La opcion ingresada no es valida, por favor intente nuevamente\n")
    break