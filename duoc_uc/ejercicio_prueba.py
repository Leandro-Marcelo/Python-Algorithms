entradaMenor = 4000
entradaAdulto = 7000
entradaAdultoMayor = 3000

totalCantidadMenores = 0
totalCantidadAdultos = 0
totalCantidadAdultosMayores = 0

acumuladorCompras = 0
totalDiaVenta = 0

count = 1

while count == 1:
    print("\nCompras Boletos")
    print("1.- Ingresar Compra")
    print("2.- Salir")
    try:
        option = int(input("Ingrese una opcion: "))
        if(option > 0 and option < 3):
            if option == 1:
                print("\nINGRESO DE COMPRA")
                menores = int(input("Ingrese cantidad menores: "))
                adultos = int(input("Ingrese cantidad de adultos: "))
                adultoMayor = int(
                    input("Ingrese cantidad de adultos mayores: "))

                if(menores > -1 and adultos > -1 and adultoMayor > -1):
                    totalMenores = entradaMenor*menores
                    totalAdultos = entradaAdulto*adultos
                    totalAdultosMayores = entradaAdultoMayor*adultoMayor
                    totalCompra = totalMenores+totalAdultos+totalAdultosMayores

                    print(
                        f"\nCompra\n-----------\n{menores} Menor(s): ${totalMenores}\n{adultos} Adulto(s): ${totalAdultos}\n{adultoMayor} Adulto Mayor(s): ${totalAdultosMayores}\n-----------\nTOTAL:    ${totalCompra}")

                    totalCantidadMenores = totalCantidadMenores + menores
                    totalCantidadAdultos = totalCantidadAdultos + adultos
                    totalCantidadAdultosMayores = totalCantidadAdultosMayores + adultoMayor

                    acumuladorCompras = acumuladorCompras + totalCompra
                else:
                    print("INGRESA SOLO NUMEROS MAYORES A -1")

            elif option == 2:

                #totalPersonas = totalCantidadMenores + \
                    #totalCantidadAdultos + totalCantidadAdultosMayores
                totalPersonas = totalCantidadMenores + totalCantidadAdultos + totalCantidadAdultosMayores

                totalDiaVenta = totalDiaVenta + acumuladorCompras

                print("\nFIN DEL DIA")
                print(f"Total personas que ingresaron: {totalPersonas}")
                print(f"Total acumulado en ventas: {totalDiaVenta}")
                break
            else:
                print("INGRESAR SOLO NUMERO 1 Y 2 !!!!")
        else:
            print("INGRESAR SOLO NUMERO 1 Y 2 !!!!!")
    except:
        print("NO INGRESAR LETRAS!!! SOLO NUMEROS (1 Y 2)")
