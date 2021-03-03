# -*- coding: cp1252 -*-
"""
#Ejercicio de eddes.
dia = 2
mes = 3
anio = 1988

dia_actual = 2
mes_actual = 3
anio_actual = 2021

cumple = True

#Calculo base de edad
edad = anio_actual - anio

#Se determina si se cumplio anio
if mes_actual <= mes and dia_actual < dia:
    #Si no ha cumplido aun, eliminamos 1 de la edad
    edad = edad - 1
    cumple = False

#Determinar mensaje en base a si ya cumplio anio
mensaje_cumple = ''
if cumple:
    mensaje_cumple = 'Ya cumplio años'
else:
    mensaje_cumple = 'No ha cumplido años'

#Determinar a que generación pertenece
if  anio >= 1920 and anio <= 1939:
    generacion = 'Generación Silenciosa'
elif  anio >= 1940 and anio <= 1959:
    generacion = 'Baby Boomers'
elif  anio >= 1960 and anio <= 1979:
    generacion = 'Generación X'
elif  anio >= 1980 and anio <= 1989:
    generacion = 'Generación Y'
elif  anio >= 1990:
    generacion = 'Generación Z'   
else:
    generacion = 'La edad no corresponde a una generación'

# Salidas
print('Tiene {} años'.format(edad))
print(mensaje_cumple)
print('Pertenece a la generación: {}'.format(generacion))
"""
#1- Operadores de asignación
"""
number = 0
while number <5:
    print(number)
    number += 1
print('Fin de ejecución')
"""
#2- Bucles while y for
"""
number = 5
var_control = 0
resultado = 0
while var_control <= number :
    resultado += var_control
    var_control += 1
print(resultado)
"""
"""
number = 5
var_control = 0
resultado = 0
while var_control <= number :
    if var_control % 2 == 0:
        resultado += var_control
    var_control += 1
print(resultado)


number = 5
var_control = 0
resultado = 0
while var_control <= number :
    resultado += var_control
    var_control += 2
print(resultado)"""

"""
number_a = 4
numero_b = 10
resultado = 0
while number_a < numero_b-1:
    number_a += 1
    print(number_a) """

"""
number_a = 4
numero_b = 10
num_max = 0
num_min = 0
numeros = ''

if number_a > numero_b:
    num_max = number_a
    num_min = numero_b
else:
    num_max = numero_b
    num_min = number_a

num_min += 1
num_max -= 1
while num_min < num_max:
    numeros += '{}, '.format(num_min)
    num_min + - 1

if num_max >= num_min:
    numeros += '{}, '.format(num_max)
    
print(number_a)"""

"""
import random
numero = random.randint(0,10)
print (numero)
intentos = 1
valor = int(input('Ingrese un numero:'))
while valor != numero:
    valor = int(input('Ingrese un numero:'))
    intentos += 1

print("intentos = {}".format(intentos)) 

for number in range(5):
    print(number)

for number in range(0,10,2):
    print(number) """


import random
numero = random.randint(1,10)
print (numero)
for num in range(1,11):
    print("{} x {} = {} ".format(numero, num, numero * num))

