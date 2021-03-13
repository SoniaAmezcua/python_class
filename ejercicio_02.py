''' 
    1303
    Ejercicio 2

    Construir un Script que dado un archivo de texto, que al leerse y procesarce se obtiene una variable data 
    que contiene la cantidad de jugadores de StarCraft por ciudad de Argentina.
    (ver variable data)

    Se solicita:
    # Calcular el total de jugadores existentes en la Argentina
    # Cual o cuales es/son la/s provincia/s con mayor cantidad de jugadores
    # Conociendo que el pais se divide en tres zonas, calcule la cantidad de jugadores por zona:
        # Norte = Formosa, Salta, Tucuman, La Rioja, Santa Fe
        # Centro = CABA, Buenos Aires, Mendoza, Cordoba
        # Sur = Chubut, Tierra del Fuego, Rio Negro

    Una vez realizado este requerimiento es necesario agregar a la lista el siguiente registro :
        # Rio Negro
        # 4 Jugadores

    Despues de agregar el elemento se requiere:
        # Calcular el total de jugadores existentes en la Argentina
        # Cual o cuales es/son la/s provincia/s con menor cantidad de jugadores
        $ Cual es la region con mayor cantidad de jugadores.

    * Este script se puede resolver con las funciones y metodos vistas en clase, no es necesario implementar algo fuera de la misma
    y en el caso de realizarlo, debera escribir un comentario de la justificacion.

    * El objetivo de este ejercicio es evaluar los conocimientos adquiridos, como a su vez las buenas practicas y la optimizacion
    de la solucion, por lo que todos estos factores seran considerados para su evaluacion.
'''

data = [
    ['CABA','Buenos Aires','Formosa','Salta','Tucuman','La Rioja','Cordoba','Mendoza','Chubut','Tierra del Fuego','Santa Fe'],
    ['45','40','0','1','2','1','4','10','1','0','2']
    ]

provincias = data[0]
cantidad_jugadores = data[1]
zonas_norte = ['Formosa', 'Salta', 'Tucuman', 'La Rioja', 'Santa Fe']
zonas_centro = ['CABA', 'Buenos Aires', 'Mendoza', 'Cordoba']
zonas_sur = ['Chubut', 'Tierra del Fuego', 'Rio Negro']

nueva_ciudad ='Rio Negro'
jugadores_rio_negro = 4
provincias_mayor_jugadores = []
provincias_menor_jugadores = []

def informacion_equipo_provincias(data_provincias, data_cantidad_jugadores):
    mayor = 0
    menor = 0
    total_jugadores = 0
    zona_norte = 0
    zona_centro = 0
    zona_sur = 0

    for index in range(len(data_cantidad_jugadores)):
        # Calcular el total de jugadores existentes en la Argentina
        total_jugadores += int(data_cantidad_jugadores[index])

        # Cual o cuales es/son la/s provincia/s con mayor cantidad de jugadores
        if int(data_cantidad_jugadores[index]) >= int(mayor) and data_provincias[index] not in provincias_mayor_jugadores:
            provincias_mayor_jugadores.append(data_provincias[index])
            mayor = data_cantidad_jugadores[index]
        # Cual o cuales es/son la/s provincia/s con menor cantidad de jugadores 
        if int(data_cantidad_jugadores[index]) <= int(menor) and data_provincias[index] not in provincias_menor_jugadores:
            provincias_menor_jugadores.append(data_provincias[index])
            menor = data_cantidad_jugadores[index]

        # Cantidad de jugadores por zona:
        if data_provincias[index] in zonas_norte:
            zona_norte += int(data_cantidad_jugadores[index])
        elif data_provincias[index] in zonas_centro:
            zona_centro += int(data_cantidad_jugadores[index])
        elif data_provincias[index] in zonas_sur:
            zona_sur += int(data_cantidad_jugadores[index])
        else:
                print("Sin zona")

    #Cual es la region con mayor cantidad de jugadores
    if zona_norte > zona_centro and zona_norte > zona_sur:
        region = "Zona Norte con {} jugadores".format(zona_norte)
    elif zona_centro > zona_norte and zona_centro > zona_sur:
        region = "Zona Centro con {} jugadores".format(zona_centro)
    elif zona_sur > zona_norte and zona_sur > zona_centro:
        region = "Zona Sur con {} jugadores".format(zona_sur)
    elif zona_norte == zona_centro and zona_norte > zona_sur:
        region = "Zona Norte con {} y Zona Centro con {} jugadores".format(zona_norte, zona_centro)
    elif zona_norte ==  zona_sur and zona_norte > zona_centro:
        region = "Zona Norte con {} y Zona Sur con {} jugadores".format(zona_norte, zona_sur)
    elif zona_centro ==  zona_sur and zona_centro > zona_norte:
        region = "Zona Centro con {} y Zona Sur con {} jugadores".format(zona_centro, zona_sur)
    else:
        region = "Todos los regiones tienen los mismos jugadores"
        
        
    return [total_jugadores, provincias_mayor_jugadores, provincias_menor_jugadores, zona_norte, zona_centro, zona_sur, region]


star_craft_argentina= informacion_equipo_provincias(provincias, cantidad_jugadores)

print("Total de jugadores existentes en la Argentina: {}".format(star_craft_argentina[0]))
print("Provincia con mayor cantidad de jugadores es: {}".format(star_craft_argentina[1]))
print ("Total de jugadores Zona Norte: {}".format(star_craft_argentina[3]))
print ("Total de jugadores Zona Centro: {}".format(star_craft_argentina[4]))
print ("Total de jugadores Zona Sur: {}".format(star_craft_argentina[5]))

#agregar a la lista nuevo registro
provincias.append(nueva_ciudad)
cantidad_jugadores.append(jugadores_rio_negro)

star_craft_argentina = informacion_equipo_provincias(provincias, cantidad_jugadores)
print("\nJugadores con Rio negro")
print("Total de jugadores existentes en la Argentina: {}".format(star_craft_argentina[0]))
print("Provincia con menor cantidad de jugadores es: {}".format(star_craft_argentina[2]))
print("Regiones con mayor cantidad de jugadores: {}".format(star_craft_argentina[6]))

print ("Total de jugadores Zona Norte: {}".format(star_craft_argentina[3]))
print ("Total de jugadores Zona Centro: {}".format(star_craft_argentina[4]))
print ("Total de jugadores Zona Sur: {}".format(star_craft_argentina[5]))
