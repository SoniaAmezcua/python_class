#Crear listado de meses, días de mes, generaciones e inicialización de variables
meses = list(range(1, 13))
generaciones = {
    "generacion_silenciosa":{"anio_inicio":1920, "anio_final":1939},
    "generacion_baby_boomers":{"anio_inicio":1940, "anio_final":1959},
    "generacion_x":{"anio_inicio":1960, "anio_final":1979},
    "generacion_millenials":{"anio_inicio":1980, "anio_final":1989},
    "generacion_z":{"anio_inicio":1990}
}
"""
#Data test - generacion_silenciosa
anio_nacimiento_inferior = 1919
anio_nacimiento_inicio = generaciones['generacion_silenciosa'].get("anio_inicio")
anio_nacimiento_final = generaciones['generacion_silenciosa'].get("anio_final")
anio_nacimiento_intermedio = 1930

#Data test - generacion_baby_boomers
anio_nacimiento_inicio = generaciones['generacion_baby_boomers'].get("anio_inicio")
anio_nacimiento_final = generaciones['generacion_baby_boomers'].get("anio_final")
anio_nacimiento_intermedio = 1950

#Data test - generacion_x
anio_nacimiento_inicio = generaciones['generacion_x'].get("anio_inicio")
anio_nacimiento_final = generaciones['generacion_x'].get("anio_final")
anio_nacimiento_intermedio = 1970

#Data test - generacion_millenials
anio_nacimiento_nicio = generaciones['generacion_millenials'].get("anio_inicio")
anio_nacimiento_final = generaciones['generacion_millenials'].get("anio_final")
generacion_millenials_intermedio = 1985
"""
#Data test - generacion_z
anio_nacimiento_inicio = generaciones['generacion_z'].get("anio_inicio")
anio_nacimiento_now = 2021

#Data test - Mes
mes_nacimiento_inicio = 1
mes_nacimiento_final = 12
mes_nacimiento_inferior = 0
mes_nacimiento_superior = 13

#Data test - dia
dia_nacimiento_inicio = 1
dia_nacimiento_final = 12
dia_nacimiento_inferior = 0
dia_nacimiento_superior = 32

#Data test - Año Bisiesto
anio_nacimiento_bisiesto = 2012
anio_nacimiento = 2013
dia_nacimiento_bisiesto = 29
mes_nacimiento = 2

#Data test - texto
anio_nacimiento_texto = "2013"
dia_nacimiento_texto = "1"
mes_nacimiento_texto = "2"


#Data
dia_nacimiento = 1
mes_nacimiento = 4
anio_nacimiento = 2019