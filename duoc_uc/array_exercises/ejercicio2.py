lista=[]
while True:
    num=int(input("ingrese un numero"))
    if num != 0:
        lista.append(num)
    else:
        break
lista.sort()
print(lista)