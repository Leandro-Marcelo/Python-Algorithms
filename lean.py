asientos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
precio_asiento_normal = 78900
precio_asiento_vip = 240000

passengers = []

app = 1

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

def form_validation(*args):
    rut = int(input("Ingresar rut: "))
    nombre = input("Ingresar nombre: ")
    telefono = input("Ingresar telefono: ")
    try:
        banco = int(input("Usted es usuario de 'bancoDuoc'? (Si = 1) (No = 0)"))
    except:
        print('Opción Inválida - Intente Nuevamente')
    if banco == 1:
        banco = True
    if banco == 0:
        banco = False
    print('Asientos Disponibles')
    print(asientos)
    try:
        asiento_escogido = int(input())
    
    """ se pide los datos del usuario, se muestra los asientos disponibles, se guarda el asiento y los datos del usuario"""

while app == 1:
    option = menu("Ver asientos disponibles", "Comprar asiento", "Anular vuelo", "Modificar datos de pasajero", "Salir")
    if option == 1:
        print(asientos)
    if option == 2:
            
    if option == 3:
            
    if option == 4:

    if option == 5:
    

  