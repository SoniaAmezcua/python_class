import random
lista = [] 
for i in range(1,10):
    lista.append(random.randint(1,9))

#lista = [1,2,3,4,5,6,7,8,9] 
print('Mi lista es {} '.format(lista))
           
repetido = 0 
countador = 0
while countador < len(lista):
    if lista.count(lista[countador]) > 1:
         repetido = lista[countador] 
         break
    countador += 1


if repetido != 0:    
    print("El numero repetido es: {}".format(repetido))
else:
    print("No existen números repetidos")