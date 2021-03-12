import random
lista = [] 
#lista = list()
for i in range(1,10):
    lista.append(random.randint(1,9))

#lista = [1,2,3,4,5,6,7,8,9] 
print('Mi lista es {} '.format(lista))
           
repetido = False
countador = 0
while countador < len(lista):
    if lista.count(lista[countador]) > 1:
         repetido = True
         print("El numero repetido es: {}".format(lista[countador])) 
         break
    countador += 1

if not repetido:
    print("No existen números repetidos")