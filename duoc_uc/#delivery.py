#delivery

#precios
churrasco = 1500
completo = 1000
vegetariano = 2000
barros_luco = 3000
total = 0

#flags
chu1 = False
com1 = False
veg1 = False
bar1 = False
cupon = False

print("11. Churrasco \n22. Completo \n33. Vegetariano \n44. Barros luco")
pedido = input("Ingrese el número de lo que va a querer en orden y separados por comas: ")

if pedido == "11":
    chu1 = True
if pedido == "22":
    com1 = True
if pedido == "33":
    veg1 = True
if pedido == "44":
    bar1 = True
if pedido == "11,22":
    chu1 = True
    com1 = True
if pedido == "11,33":
    chu1 = True
    veg1 = True
if pedido == "11,44":
    chu1 = True
    bar1 = True
if pedido == "22,33":
    com1 = True
    veg1 = True
if pedido == "22,44":
    com1 = True
    bar1 = True
if pedido == "33,44":
    veg1 = True
    bar1 = True
if pedido == "11,22,33":
    chu1 = True
    com1 = True
    veg1 = True
if pedido == "11,22,44":
    chu1 = True
    com1 = True
    bar1 = True
if pedido == "11,33,44":
    chu1 = True
    veg1 = True
    bar1 = True
if pedido == "22,33,44":
    com1 = True
    veg1 = True
    bar1 = True
if pedido == "11,22,33,44":
    chu1 = True
    com1 = True
    veg1 = True
    bar1 = True

#calcula total a pagar (no incluye descuento)
if chu1:
    cant_chu = int(input("¿Cuántos Churrascos va a querer? "))
    total_chu = churrasco*cant_chu
    total = total+total_chu
if com1:
    cant_com = int(input("¿Cuántos Completos va a querer? "))
    total_com = completo*cant_com
    total = total+total_com
if veg1:
    cant_veg = int(input("¿Cuántos Vegetarianos va a querer? "))
    total_veg = vegetariano*cant_veg
    total = total+total_veg
if bar1:
    cant_bar = int(input("¿Cuántos Barros Luco va a querer? "))
    total_bar = barros_luco*cant_bar
    total = total+total_bar

#define si el cliente tiene descuento
descuento = input("¿Usted tiene un cupon de descuento? ")

if descuento == "si":
    cupon = True

elif descuento == "no":
    print(f"El total a pagar es: {total}")

if cupon:
    total = int(total*0.9)
    nro_cupon = input("Ingrese su cupon: ")
    print(f"Usted tiene un 10% de descuento, el total a pagar es: {total}")