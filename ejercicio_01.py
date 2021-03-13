import random
#import numpy as np

lista_sudoku = [] 
contador = 1
while contador < 10:
    valor = random.randint(1,9)
    if valor not in (lista_sudoku):
        lista_sudoku.append(valor)  
        contador += 1  

print('Lista Sudoku: {}'.format(lista_sudoku))

# #Me apoye de la libreria numpy para hacer el split en 3 secciones y poder manejarlos de manera independiente
# lista_sudoku_split= np.array_split(lista_sudoku, 3)
# print(lista_sudoku_split[0])
# print(lista_sudoku_split[1])
# print(lista_sudoku_split[2])

# sum_bloque_a = sum(lista_sudoku_split[0])
# sum_bloque_b = sum(lista_sudoku_split[1])
# sum_bloque_c = sum(lista_sudoku_split[2])

#Con lo aprendido en clase hoy
print(lista_sudoku[:3])
print(lista_sudoku[3:6])
print(lista_sudoku[-3::])

sum_bloque_a = sum(lista_sudoku[::3])
sum_bloque_b = sum(lista_sudoku[3:6])
sum_bloque_c = sum(lista_sudoku[-3::])

print('Sumatoria: {}'.format(sum(lista_sudoku)))
print('Sumatoria de A: {}'.format(sum_bloque_a))
print('Sumatoria de B: {}'.format(sum_bloque_b))
print('Sumatoria de C: {}'.format(sum_bloque_c))

if sum_bloque_a > sum_bloque_b and sum_bloque_a > sum_bloque_c:
    print("Bloque A es mayor")
elif sum_bloque_b > sum_bloque_a and sum_bloque_b > sum_bloque_c:
    print("Bloque B es mayor")
elif sum_bloque_c > sum_bloque_a and sum_bloque_c > sum_bloque_b:
    print("Bloque C es mayor")
elif sum_bloque_a ==  sum_bloque_b and sum_bloque_a > sum_bloque_c:
    print("Bloque A y B son mayores")
elif sum_bloque_a ==  sum_bloque_c and sum_bloque_a > sum_bloque_b:
    print("Bloque A y C son mayores")
elif sum_bloque_b == sum_bloque_c and sum_bloque_b > sum_bloque_a:
    print("Bloque B y C son mayores")
else:
    print("Todos los bloques son iguales")






