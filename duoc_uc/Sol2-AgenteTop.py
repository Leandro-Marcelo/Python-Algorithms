#AgenteTop
visita=[]
while (True):
    print("1.- Registrar visita")
    print("2.- Consultar datos de una visita")
    print("3.- Registrar tipo de visita")
    print("0.- Salir")
    try:
        op=int(input("Opcion ? " ))
        if (op==1):
            #valida rut
            while (True):
                try:
                    rut=int(input("Rut visita ? "))
                    if (rut>=5000000 and rut <=99999999):
                        print("+++ rut OK +++")
                        break
                    else:
                        print("--- rut fuera de rango ---")
                except:
                    print("...Error, Rut debe ser numérico")
            # Valida Nombre
            nom=""       
            while (len(nom)<5):
                nom=input("Nombre visita ? : ")
                if (len(nom)<5):
                    print("Nombre debe tener al menos 5 caracteres")
            #Valida edad
            while (True):
                try:
                    edad=int(input("Edad visita ? : "))
                    if (edad>=1 and edad<100):
                        break
                    else:
                        print("..Edad debe estar en rango 1 a 99")
                except:
                    print("Error, edad debe ser numerica")
            #Valida relación familia (en minusculas)
            while (True):
                fam=input("Visita es familiar ? : ")
                if (fam=="s" or fam=="n"):
                    break
                else:
                    print("Debe indicar s o n para relación de parentezco")
            #Agrega datos al registro
            visita.append([rut,nom,edad,fam])
            print("...Visita registrada")
            print([visita])
            print(".............................")
        elif (op==2):
            existe=False
            while (True):
                try:
                    rut=int(input("Rut visita2 ? "))
                    if (rut>=5000000 and rut <=99999999):
                        print("+++ rut OK2 +++")
                        print(visita)
                        break
                    else:
                        print("--- rut fuera de rango2 ---")
                except:
                    print("...Error, Rut debe ser numérico2")
            # Se recorre lista
            for i in range(len(visita)):
                if (rut==visita[i][0]):
                    existe=True
                    pos=i
                    break
                if (existe):
                    reg=input("Ingrese tipo de visita: ")
                    visita[pos].append(reg)
                    print("...Tipo visita registrado")
                    #
                    print(visita[pos])
                    #
                else:
                    print("Visita sin registro")
            print("...222")
        elif (op==3):
            existe=False
            while (True):
                try:
                    rut=int(input("Rut visita3 "))
                    if (rut>=5000000 and rut <=99999999):
                        print("+++ rut OK3 +++")
                        print(visita)
                        break
                    else:
                        print("--- rut3 fuera de rango2 ---")
                except:
                    print("...Error, Rut3 debe ser numérico3")
                # Se recorre lista
            for i in range(len(visita)):
                if (rut==visita[i][0]):
                    existe=True
                    pos=i
                    print(pos)
                    print(".......")
                    break
            if (existe):
                reg=input("Ingrese tipo de visita: ")
                visita[pos].append(reg)
                print("Tipo registrado OK")
            else:
                print("Visita sin registro")
                print("...333")
        elif (op==0):
            print("...The End")
            break
        else:
            print("...Favor ingrese opción válida")
    except:
        print("##########################################")
        print("...Opción errónea, he vuelto al menu ppal.")
        print("##########################################")