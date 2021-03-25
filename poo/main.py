# Una clase es una plantilla para crear un objeto
# Cuando quieres encapsular es con doble guíon 
# Cuando hay herencia para que los hijos accedan hay que hacerlo con un solo guíon
# Desde afuera no puedo cambiar atributos
# Por medio de la "API" Seter 

from car import Car 

auto = Car('Mercedes', 'Verde')

print(auto.get_marca())
print(auto.get_color())
print(auto.get_neumaticos())
print(auto.get_nombre_motor())
#auto.__set_color('Gris')



