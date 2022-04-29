""" 
La tienda “PetOnLine” ofrece a sus clientes una cama estándar para mascotas pequeñas cuyo pecio unitario a cliente es de $100.

Para incentivar las ventas, la tienda ha desarrollado una campaña promocional en la que ofrece atractivos descuentos por compras al por mayor, bajo la siguiente estructura:

  10% de descuento por compras sobre 10 unidades
  20% de descuento por compras entre 20 y 29 unidades
  30% de descuento por compras por sobre 30 unidades

Usando la herramienta PSeInt, escriba un algoritmo para calcular automáticamente el monto a pagar dependiendo de la cantidad de camitas solicitadas.
"""

bedPrice = 100

def discount(beds):
  if (beds <= 10):
    return f'total price: {beds * bedPrice} usd'
  
  if (beds > 10 and beds < 20):
    return f'total price: {(beds * bedPrice   -  ( (beds * bedPrice * 10)//100))} usd'

  if (beds >= 20 and beds <= 29):
    return f'total price: {(beds * bedPrice   -  ( (beds * bedPrice * 20)//100))} usd'

  return f'total price: {(beds * bedPrice   -  ( (beds * bedPrice * 30)//100))} usd'
  

print(discount(30))


