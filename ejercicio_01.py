import random
import numpy as np

lista_sudoku = [] 
contador = 1
while contador < 10:
    valor = random.randint(1,9)
    if valor not in (lista_sudoku):
        lista_sudoku.append(valor)  
        contador += 1  

print('Lista Sudoku: {}'.format(lista_sudoku))

#Me apoye de la libreria numpy para hacer el split en 3 secciones y poder manejarlos de manera independiente
newarr = np.array_split(lista_sudoku, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])

sum_bloque_a = sum(newarr[0])
sum_bloque_b = sum(newarr[1])
sum_bloque_c = sum(newarr[2])

print('Sumatoria de A: {}'.format(sum_bloque_a))
print('Sumatoria de B: {}'.format(sum_bloque_b))
print('Sumatoria de C: {}'.format(sum_bloque_c))

if sum_bloque_a > sum_bloque_b and sum_bloque_c:
    print("Bloque A es mayor")
elif sum_bloque_b > sum_bloque_a and sum_bloque_c:
    print("Bloque B es mayor")
elif sum_bloque_c > sum_bloque_a and sum_bloque_b:
    print("Bloque C es mayor")
else:
    print("Todos los bloques son iguales")






