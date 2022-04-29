""" 
Construya un programa en PSeInt que, lea 2 números y a partir de un Menú de 4 opciones, permita al usuario elegir: sumar, restar, multiplicar o dividir dichos números. Se recomienda utilizar la sentencia Según.
"""


def numberOperations(num1, num2, operation):
  print(type(num1))
  print(type(num2))
  print(type(operation))

  if (operation == "add"):
    return num1 + num2

  if (operation == "subtract"):
    return num1 - num2
  
  if (operation == "multiply"):
    return num1 * num2
  
  if (operation == "divide"):
    return num1 // num2

  return f'xd'

print(numberOperations(1,2,"divide"))

""" 
Una palabra palíndormo es aquella que se escribe igual en un sentido u otro, por ejemplo: radar, rallar, aviva, salas, etc. Se pide usted haga un programa que lea un número de 5 cifras e indique si es o no palíndromo.
 """

def isCapicua(num):
  n=0
  parserToString = str(num)
  longitud = len(parserToString)
  arr = []
  while(n < longitud):
    arr.append(parserToString[n])
    n += 1
  print(arr) # ['1', '0', '0']

isCapicua(100) 