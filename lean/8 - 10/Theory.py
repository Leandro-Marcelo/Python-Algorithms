# loop for

for el in "elemento":
    print(el) # e l e m e n t o  => imprime cada letra por iteración

for i in range(1,10):
    print(i) # 0 1 2 3 .... 9 => imprime cada numero por iteración

# esta wea es un forEach xd
for i in ["dog", "cat", "cocodrile", "canary"]:
    print(i) # dog cat cocondrile canary => imprime cada numero por iteración

for i in (1,2,3):
    print(i) # 1 2 3 

# Si yo solamente quiero saber si se cumple o no la condición representando por un booleano, lo unico que voy hacer es agregar una flag para que
# cuando se cumpla la condición modifique la variable de false a true y luego utilizo ese True dentro de un if y me diga tal cosa se cumplió