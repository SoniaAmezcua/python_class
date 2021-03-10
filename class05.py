# -*- coding: cp1252 -*-
import random
"""
numero = random.randint(1,10)
print ("El número es {}:".format(numero))
for num in range(1, numero + 1):
    print("*" * num)
"""

#Break
"""
for numero in range(1,10):
    if numero % 2 == 0:
        print('Tenemos un número par: {}, no continuamos'.format(numero))
        break
    print('Este número no es par: {}'.format(numero))"""

"""numero = 1
while numero % 2 != 0:
     print('Este número no es par: {}'.format(numero))
     numero += 1
print('Tenemos un número par: {}, no continuamos'.format(numero))"""


"""numero = 1
while numero < 10:
    if numero % 2 == 0:
        print('Tenemos un número par: {}, no continuamos'.format(numero))
        break
    print('Este número no es par: {}'.format(numero))
    numero += 1 """

#Continue
"""
result = 0
for numero in range(1,10):
    if numero % 2 == 0:
        print('Tenemos un número par: {}, y los numeros pares no se procesan'.format(numero))
        continue
    result += numero
print(result)

"""
"""
for numero in range(0, 99, 2):
    if numero % 3 == 0:
        continue
    print(numero)

num = 0
while num < 100:
    if numero % 3 != 0:
        print (num) """
 
"""
num_aleatorio = random.randint(1, 20)
num_aleatorio = num_aleatorio * 2
result = 0
for numero in range(1, 99):
    if numero == num_aleatorio:
        break
    result += numero
print(result)
"""
"""
numero = random.randint(1, 20) 
numero *= 2
num = 2
result = 1
print(numero)
while num != numero:
    result += num
    num += 1
print(result)
"""

my_lista = [1,2,3,4,5,6]
my_lista.append(8)
print(len(my_lista))

print(my_lista[len(my_lista)-1])





