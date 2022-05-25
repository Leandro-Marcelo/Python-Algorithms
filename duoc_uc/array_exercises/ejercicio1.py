""" Ingrese un número por teclado y guarde en una lista su tabla de multiplicar hasta el 10. 
Ejemplo, si ingresa el número 3, la lista debe contener: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30
 """

def tabla_multiplicar(n):
    arr = []
    for i in range(1,11):
        arr.append(i*n)
    return arr

print(tabla_multiplicar(3))