""" print("lean"[-4]) 

# por lo que para acceder a lean a través del index sería así

# 0    1/-3   2/-2     3/-1
# l       e         a         n

# tambien podemos acceder a segmentos o rebanadas de los strings

print("leandro"[0:4]) #lean ya que el último no esta incluido también se pudo escribir así "leandro"[:4]

print("leandro"[2:5]) # and

print("leandro"[4:]) # dro

a = "rosa"
b = "saco"

c = a[:2] + b[:2]
print(c) # rosa 

Además los strings son inmutables, es decir, tu no puedes "leandro"[0] = "s"   esto te tiraría un error, lo que si puedes hacer es, imaginate que "leandro" esta dentro de una variable entonces puedes reasignarle el valor a esa variable pero tampoco podrías hacer variable[0] = s TAMPOCO SE PUEDE PORQUE ES LO MISMO QUE LO DEL PRINCIPIO
"""

""" eso nos permite hacer comentarios de varias lineas pero tambien cadenas de texto de varias lineas """

# esto es como cuando usamos include en JS
print("a" in "artefacto") # true

print("a" not in "artefacto") # false

print("facto" not in "artefacto") # false

# Las tuplas, es un tipo de dato donde podemos almacenar distintos tipos de datos primitivos y es de tipo inmutable como lo es un string, es decir, que no pueden ser modificadas

new_tuple = (1,2,"3",True, (1,2,3))

# como las tuplas también son un tipo de dato secuencia al igual que los strings, podemos concatenarlas entre ellas, no podemos concatenar un string con una tupla

t_1 = (1,2,3) 
t_2 = (4,5,6)

t_result = t_1 + t_2
print(t_result) # (1, 2, 3, 4, 5, 6)

# podemos utilizar el operador de indexación

print(t_1[2]) # 3

# podemos agarrar segmentos o trozos 

print(t_result[2:5]) # 3 4 5

# podemos saber la longitud de una tupla

print(len(t_result)) # 6

#                                                         Lists

# con las listas vamos a poder hacer las mismas operaciones que haciamos con las cadenas y tuplas, pero ademas vamos a poder modificarlas, caracteristica que las tuples y los strings no tienen o no pueden. Por lo tanto, podemos quitar elementos, añadir elementos, modificar elementos.
pets = ["cat", "dog", "canary", "crocodile"]


pets[3] = "turtle" # si intentamos esto a una tupla, no nos lo va a permitir

print(pets) # ['cat', 'dog', 'canary', 'turtle']

# A la hora de elegir una tupla o una lista, ten en cuenta que las tuplas van a ser mas rápidas que las listas y por tanto si vamos a tener una tupla de millones de elementos pues se va a notar la diferencia frente a una lista, si tiene pocos elementos no se va a notar esa diferencia y en cambio las listas van a ser mucho mas versatiles, van a tener muchos mas usos que las tuplas. Pero también hay un elemento importante dentro de las límitaciones de las tuplas que nos puede servir, como no son modificables podemos utilizar esa limitación como elemento de seguridad, por lo tanto, cuando vayamos a crear una secuencia de elementos que no tengamos pensado modificar a lo largo del programa, nos podrá convenir utilizar una tupla, ya que ninguna operación la va a modificar 

# concatenando lists and tuples

my_tuple = ()
#acá tambien podemos usar my_tuple+=(1,2,3)
my_tuple = my_tuple + (1,2,3)

print(my_tuple) # (1,2,3)

my_list = []
#acá tambien podemos usar my_list+=[4,5,6]
my_list = my_list + [4,5,6]
print(my_list)

# no es que cree 3 listas sino que concatena la misma lista 3 veces

numbers = [1,2,3]
numbers *= 3 # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(numbers)

#                                                         Range

#Range almacena secuencias de números enteros pero solo como intervalo sin llegar a mostrar cada uno de los números de esa secuencia

# range(10) iría del 0 al 9

# 5 in range(10) => True, acá estamos diciendo el 5 esta entre el 0 y el 9 

my_range = range(10, 21)

print(20 in my_range) # True

# range recibe un tercer argumento que sería el salto, 

my_new_range = range(1, 11, 2)
print(3 in my_new_range) # True
print(5 in my_new_range) # True
print(7 in my_new_range) # True
print(8 in my_new_range) # False












import math # Si solo vamos a utilizar algunas funciones del módulo math, podemos importar solamente esas funciones de esta manera from math import pi, sqrt     OJO de esta manera para acceder al valor de la función pi ya no sería math.pi sino simplemente pi y eso implicaría que no podes declarar una variable como pi

# No muestra todas las funciones que tiene este módulo math
# print(dir(math))

# También podríamos definir PI como una constante y esta tendría que ir en uppercase por convención

# Módulo random, 
import random

print(dir(random))

# random.randint(1,10) nos devolverá un número random [1,10]

a = range(10) # 0, 1, 2, 3 .... 9

print(10 in a) # false