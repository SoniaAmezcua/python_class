#Listas-Ejercico 2 - Forma A
"""import random
lista = [] 
#lista = list()
for i in range(1,10):
    lista.append(random.randint(1,9))

#lista = [1,2,3,4,5,6,7,8,9] 
print('Mi lista es {} '.format(lista))
           
repetido = False
indice = 0
lista.sort()

while indice < len(lista) -1 and not repetido:    
    if lista[indice] == lista[indice + 1]:
        print('El numero {} esta repetido'.format(lista[indice]))
        repetido = True
    indice += 1

if not repetido:
    print('No hay numeros repetidos')


#Listas-Ejercico 2 - Forma B
           
repetido = False
indice = 0
lista.sort()

while indice < len(lista) -1 and not repetido:  
    value =  lista[indice] 
    if lista[indice] == lista[indice + 1]:
        print('El numero {} esta repetido'.format(lista[indice]))
        repetido = True
    indice += 1

if not repetido:
    print('No hay numeros repetidos')
"""

cards_poker_planning = [0,0.5,1,2,3,5,8,13,20,40,100] 
print('Poker Planning {} '.format(cards_poker_planning))

lista_pares = [item for item in cards_poker_planning if item%2 == 0]

lista_divisibles = []
for item in cards_poker_planning:
    if item%2 == 0:
        lista_divisibles.append(item)

countador = 0
indice = 2
while indice < len(cards_poker_planning):
    if cards_poker_planning[indice]%cards_poker_planning[indice-1]==0:
        countador += 1
    indice += 1

print("Cúantos son pares: {}".format(len(lista_pares)))
print("Cúantos n+umero son divisibles por el anterior: {}".format(countador))
print("Sumatoria de todos los números es : {}".format(sum(cards_poker_planning)))
