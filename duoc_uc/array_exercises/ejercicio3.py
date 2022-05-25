import statistics


lista=[]
a=1
for a in range (10):
    num=int(input("ingrese un numero"))
    lista.append(num)
suma=sum(lista)
prom=statistics.mean(lista)

print("la lista ingresada es\n",lista)
print("la suma es \n",suma)
print("el promedio es\n",prom)