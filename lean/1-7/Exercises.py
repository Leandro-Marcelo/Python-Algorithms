from cmath import sqrt
import math


""" #                                                         Programa que calcula el perimetro de una circunferencia

radio = float(input(f'Dime el radio de la circunferencia: '))

perimetro = 2 * math.pi * radio

print(f'El perímetro es:', perimetro)  """

""" #                                                         Programa que calcula el área de un circulo

radio = float(input(f'Dime el radio del círculo: '))

area = math.pi * (radio**radio)

print(f'El area es:', area)  """

""" #                                                         Programa que calcula la hipotenusa dado el CA y el CO

ca = float(input(f'Dime el cateto adyacente: '))
co = float(input(f'Dime el cateto opuesto: '))

hip = math.sqrt((ca**2) + (co**2))

print(f'La hip es: {hip}') """

""" #                                                         Programa que calcula el perímetro de la elipse

r = float(input(f'Dime el valor de r: '))
s = float(input(f'Dime el valor de s: '))

p = 2 * math.pi * math.sqrt(((r**2) + (s**2)) / 2)

print(f'el resultado es: {p}') """

""" #                                                         Intercambiar valores entre dos variables

x = 100
y = 200
aux = x

x = y
y = aux

print(f'el nuevo valor de x: {x} y el nuevo valor de y: {y}')

# Otra forma que tiene python de resolver esto sería
# definimos 

u, v = 100, 200

# intercambiamos
v, u = u, v

print(f'el nuevo valor de u: {u} y el nuevo valor de v: {v}')

# ¿Por qué no aprendemos esto directamente? porque el objectivo es aprender a programar, es decir, desarrollar una lógica a la hora de programar y aprender a programar es distinto a aprender una característica propia de un lenguaje en concreto como puede ser python porque si no sabes estas técnicas/estrategias y luego quieres aprender otro lenguaje de programación (que es mi caso) que no dispone de esta característica la vas a extrañar y probablemente te cueste mucho mas llevarla a cabo.  """

""" #                                                         Programa que te pide que te inventes una contraseña y que luego la repitas dos veces más. Depués comprueba que lo has hecho correctamente

password = input("password: ")
repeatedPassword = input("repeate password: ")

if (password == repeatedPassword):
  print("Ingresas al programa") """

""" # while es lo mismo que la palabra reiterar en castellano, por ejemplo, no me hagas reiterar lo que te ordené, entonces el while va a ser ejecutar un código de forma repetida, por eso la sentencia while se le conoce también como una sentencia interativa  

# Programa que muestre en pantalla una secuencia de números del 1 al 10

n = 1
while(n <= 10): # 1, 2, 3,..... 10
  print(n)
  n = n + 1 """

""" # Programa que imprime del 20 al 0

n = 20
while(n >= 0):
  print(n)
  n = n - 1 """

""" # Programa que pregunte al usuario si quiere seguir jugando

print("let's play")

playing = "y"

while(playing == "y"):
  print(f'playing')
  option = input('do you wanna continue playing? (yes = y) (no = n): ')
  if (option == "n" or option == "y"):
    playing = option
  else:
    print(f'enter "y" or "n" please') """
  
""" #                                                         Programa que te pide que adivines un número del 1 al 10 y te pide números constantemente hasta que los adivines.  Añade un contador que te diga los intentos que has necesitado

numero_a_adivinar = 6
intentos = 0
intento_de_numero = 0
# otra lógica hubiera sido          intento_de_numero != numero_a_adivinar
while(not (intento_de_numero == numero_a_adivinar)):
  intentos = intentos + 1
  print("Adivina el número")
  intento_de_numero = int(input())

 
print(f'¡Adivinaste!, te tomo {intentos} intentos') """

""" #                                                         Mostrar en pantalla las letras que forman la palabra "mariposa"

n = 0
cadena = "mariposa"
longitud  = len(cadena) # 8

# acá la lógica también pudo ser n < longitud ya que así no toma el 8 ya que el 8 no es menor a 8
while(n<= longitud - 1):
  print(cadena[n])
  n += 1 """

""" #                                                         Comprobar cuántas veces aparece el carácter "o", con o sin tilde, en la siguiente cadena de caracteres 

text = "Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendia había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo"

i = 0
str_length = len(text)
cont = 0

while(i < str_length):
  if (text[i] == "o" or text[i] == "ó"):
    cont += 1
  i += 1

print(f'La "o" o "ó" aparecen {cont} veces') """

""" #                                                         Programa que te dice la cantidad de vocales que tiene una palabra

# una forma de resolver esto sería 

# if (word[i] == "a" or word[i] == "á" or .... ) si bien esto funcionaría, es bastante tedioso, aquí es donde surge el utilizar el in así como también usamos en MongoDB para filtrar

word = input("enter a word: ")

vowels = "aeiouáéíóúü"
i = 0
vowel_numbers = 0

while(i < len(word)):
  if (word[i] in vowels):
    vowel_numbers += 1
  i += 1

print(f'El número de vocales que tiene la palabra ingresada es de: {vowel_numbers}') """

""" #                                                         Programa que te dice la cantidad de vocales y consonantes que tiene una palabra

word = input("enter a word: ")

vowels = "aeiouáéíóúü"
consonants = "bcdfghjklmnñpqrstvwxyz"
i = 0
vowel_numbers = 0
consonant_numbers = 0

while(i < len(word)):
  if (word[i] in vowels):
    vowel_numbers += 1
  if (word[i] in consonants):
    consonant_numbers += 1 
  i += 1

print(f'La palabra ingresada tiene: {vowel_numbers} vocales y {consonant_numbers} consonantes') """

""" #                                                         Tenemos tres tuplas: Crea una tupla a partir de ellas que contenga las mascotas

mamiferos = ("tigre", "gato", "león")
aves = ("aguila", "buitre", "canario")
reptiles = ("tortuga", "serpiente")

# pets = mamiferos[1] + aves[2] + reptiles[0]  MALO, nos imprimiría gatocanariotortuga ya que estamos obteniendo los strings y luego concatenandolos.

# Para solucionar lo de arriba, debemos agarrar segmentos para que nos devuelvan tuplas ya que estamos obteniendo estos elementos de una tupla y luego cuando concatenemos tuplas todo se almacene en una sola tupla
pets = mamiferos[1:2] + aves[2:] + reptiles[0:1]

print(pets) # ("gato", "canario", "tortuga")

# otra forma de resolverlo hubiera sido

pets2 = (mamiferos[1], aves[2], reptiles[0])

# otra forma de resolverlo hubiera sido

pets3 = (mamiferos[1], ) + (aves[2], ) + (reptiles[0], ) """

""" #                                                         Crea una lista que contenga los números enteros del 1 al 100 utilizando un bucle while, y partiendo de una lista vacía

new_list = []
i = 1

while(i <= 100):
  new_list = new_list + [i]
  i = i + 1

print(new_list) """

""" #                                                         Programa que pida un número entero que esté en el intervalo del 18 al 25, y que siga pidiendo números mientras te mantengas en ese intervalo

num = int(input(f'Ingresa un número entero entre el 18 y el 25: ')) # OJO acá es importante pedir un número entero porque si fuera de tipo decimal, ya no podríamos utilizar range, ya que range solo toma la secuencia considerando solo los números enteros

while(num in range(18, 26)):
  print(f'Estamos en el rango')
  num = int(input(f'Ingresa nuevamente un número entero entre el 18 y el 25: '))
else:
  print(f'Estamos fuera del rango')

# Otra manera de resolverlo pero utilizando flag

is_in_range = True

while(is_in_range):
  num = int(input(f'Ingresa un número entero entre el 18 y el 25: '))
  if (num in range(18,26)):
    print(f'Estamos en el rango')
  else:
    print(f'Estamos fuera del rango')
    is_in_range = False """

#                                                         Juego "Ruleta de los colores" 1: El juego nos pide un color, 2: Si acertamos, nos lo muestra, nos da los puntos y nos pide el otro color, 3: Si no acertamos, nos lo muestra, nos da los puntos conseguidos y se acaba el programa.

colors = ["red", "white", "lime", "green", "purple", "black"]
points = 0 

playing = True

while(playing):
  color = input(f'Ingresa un color: ')
  if (color in colors):
    points += 1
  else:
    playing = False
    print(f'Has perdido, has conseguido {points}')