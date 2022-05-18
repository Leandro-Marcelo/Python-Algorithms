""" #                                                         Programa que va mostrando en pantalla en una cuenta atrás los números del 10 al 0.
# Supongo que por defecto el tercer argumento es 1 por eso siempre va a 0 hacia +00 (infinito)
for i in range(10, -1, -1):
    print(i) # 10 9 8 7 .... 0  

# este range iría de [0,10]
for i in range(11):
    # empieza con 10 - 0 hasta 10 - 10 y ya todo sale igual
    print(10-i) # 10 9 8 .... 0 """

""" #                                                         Programa que te pide 5 números y los va sumando. Al final te muestra el resultado
# esto podríamos verlo como un reduce
total = 0
for i in range(5):
    total += int(input(f'Enter a number: '))

print(total) """

""" #                                                         Programa que va pidiendo números y los va sumando hasta que alcanza 100 o más. Entonces para y muestra el total.
goal = 100
total = 0
while(total < goal):
    total += int(input(f'Enter a number: '))
print(total) """

""" #                                                         Saber si en la lista/array contiene la letra "l"

letters = ["a", "l", "c", "z", "w"]

if "l" in letters:
    print(f'la letra "l" si esta incluido en letters')

# otra forma de resolverlo utilizando el bucle for

for i in letters:
    if i == "l":
        print(f'la letra "l" si esta incluida en letters')
    else:
        print(f'la letra "l" no esta incluida en letters') """

""" #                                                         Programa que pide un número al usuario. Si ese número sumado con algun número de la lista dada es igual a 100, el programa tendrá que decir que el número cumple la condición

my_list = [28, 36, 43, 52, 61, 75, 84, 97]

num = int(input())

for el in my_list:
    if ((el + num) == 100):
        print(f'El número ingresado cumple la condición')

# otra manera de resolverlo, prácticamente aplicó matematica, lo que esta sumando pasa restando, lo que esta multiplicando pasa dividiendo, entonces
# recordando la logica anterior el + num = 100 <=> el = 100 - num , :)
if ((100-num) in my_list):
    print(f'El número ingresado cumple la condición') """

""" #                                                         Programa que comprueba cuántas veces está un número en una lista dada

my_list = [28,36,43,52,61,43,75,84,43,97]
cont = 0
num = int(input())

for el in my_list:
    if (el == num):
        cont += 1

print(cont) """

""" #                                                         Tenemos una tupla con los meses del año. Queremos saber qué meses tienen en su nombre la letra "b"

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

months_with_b = ()
for month in months:
    if "b" in month:
        months_with_b += (month, )

print(months_with_b)

# Otra forma de resolverlo
cumple_la_condicion = []
for month in months:
    if "b" in month:
        cumple_la_condicion.append(month)

print(cumple_la_condicion) """

#                                                         Programa que comprueba si un numero en específico está dentro de la lista y nos dice en qué posición (index) se encuentra

my_list = [2,5,90,23,45,87,54,11,38]
index = 0
num = 11

for el in my_list:
    if (num == el):
        print(num, index)
    index += 1

# otra manera de resolverlo

for i in range(len(my_list)):
    if my_list[i] == num:
        # si te refieres al indice de un array pues este empieza en 0, si te refieres simplemente a la posicion entonces el primer elemento es la posicion 1 por lo que
        # seria i + 1
        print(num, i)




