data = [
    ['CABA','Buenos Aires','Formosa','Salta','Tucuman','La Rioja','Cordoba','Mendoza','Chubut','Tierra del Fuego','Santa Fe'],
    ['45','40','0','1','2','1','4','10','1','0','2']
    ]

total_jugadores = 0
zona_norte = 0
zona_centro = 0
zona_sur = 0

nueva_ciudad ='Rio Negro'
jugadores_rio_negro = 4

for index in range(len(data[1])):
    total_jugadores += int(data[1][index])
    if data[0][index] in ['Formosa', 'Salta', 'Tucuman', 'La Rioja', 'Santa Fe']:
        zona_norte += int(data[1][index])
    elif data[0][index] in ['CABA', 'Buenos Aires', 'Mendoza', 'Cordoba']:
        zona_centro += int(data[1][index])
    elif data[0][index] in ['Chubut', 'Tierra del Fuego', 'Rio Negro']:
        zona_sur += int(data[1][index])
    else:
        print("Sin zona")


print("Jugadores sin Rio negro")
print ("Total de jugadores existentes en la Argentina {}".format(total_jugadores))
print ("Total de jugadores Zona Norte {}".format(zona_norte))
print ("Total de jugadores Zona Centro {}".format(zona_centro))
print ("Total de jugadores Zona Sur {}".format(zona_sur))


data[0].append(nueva_ciudad)
data[1].append(jugadores_rio_negro)


print("Jugadores con Rio negro")
print ("Total de jugadores existentes en la Argentina {}".format(total_jugadores + jugadores_rio_negro))
print ("Total de jugadores Zona Norte {}".format(zona_norte))
print ("Total de jugadores Zona Centro {}".format(zona_centro))
print ("Total de jugadores Zona Sur {}".format(zona_sur + jugadores_rio_negro))


