# -*- coding: cp1252 -*-
#Modificación de listas
# my_list = [4,5,6,7]
# my_list[2]= 0

#obtener último valor de la lista
# print(my_list[len(my_list)-1])


#Agregar un nuevo item
# my_list.append(10)
# my_list.append("Hola")

#Eliminar item
# my_list.pop(2)
# print(my_list)

# print(my_list[3])
# del my_list[2]
# print(my_list[2])

#obtener último valor de la lista con indice negativo
# print(my_list[-1])


# my_list = [-2,10,4,9,6,7,0]
# print(my_list)
# my_list.sort()
# print(my_list)

# my_list.reverse()
# print(my_list)

#Ejercicio 1
#import random

# my_list = [1,2,3,4,5]
# print('El tamaño de la lista es: {}'.format(len(my_list)))

# numero = random.randint(1,10)
# print('El random es: {}'.format(numero))

# my_list.append(numero)
# print(my_list)

# count = 0
# while count < len(my_list) and numero <= 5:
#     print('Iteración {} del while ')
#     if numero == my_list[count]:
#         my_list.pop(count)
#         break
#     count += 1

# # if len(my_list) == 6:
# #     my_list.pop(0)

# if count == 0:
#     my_list.pop(0)
#     print('El número no esta en la lista, por lo que se elimina el primer registro')


# print('El tamaño de la lista es: {}'.format(len(my_list)))
# print(my_list)

# for index in range(0,len(my_list)-1):
#     print(index)
#     if numero == my_list[index]:
#         my_list.pop(index)
#     else:
#         my_list.pop(0)
# my_list.append(numero)

# print(my_list)
# print(len(my_list))



#Ejercicio Tarea
import random
lista = [] 
for i in range(1,10):
    lista.append(random.randint(1,9))

#lista = [1,2,3,4,5,6,7,8,9] 
print('Mi lista es {} '.format(lista))

#Con For
# repetido = 0 
# for index in range(0,len(lista)-1):
#     if lista.count(lista[index]) > 1:
#         #print("entro al for solo una vez")
#         repetido = lista[index] 
#         break
             

#Con while
repetido = 0 
countador = 0
while countador < len(lista):
    if lista.count(lista[countador]) > 1:
         #print("Entro al wile solo una vez")
         repetido = lista[countador] 
         break
    countador += 1


if repetido != 0:    
    print("El número repetido es: {}".format(repetido))
else:
    print("No existen números repetidos")