# -*- coding: cp1252 -*-
from datetime import datetime
from calendar import monthrange
from util.data.determinar_generacion import generaciones, meses, dia_nacimiento, \
    mes_nacimiento, anio_nacimiento

#Obtener fecha actual
now = datetime.now()
dia_actual = now.day
mes_actual = now.month
anio_actual = now.year

def obtener_generacion():
    #Método para obtener la generación a la cual pertences una persona de acuerdo al año de nacimiento
    if anio_nacimiento >= generaciones['generacion_silenciosa'].get("anio_inicio") and \
        anio_nacimiento <= generaciones['generacion_silenciosa'].get("anio_final"):
        generacion = "Silenciosa"
    elif anio_nacimiento >= generaciones['generacion_baby_boomers'].get("anio_inicio") and \
        anio_nacimiento <= generaciones['generacion_baby_boomers'].get("anio_final"):
        generacion = "Baby_boomers"
    elif anio_nacimiento >= generaciones['generacion_x'].get("anio_inicio") and \
        anio_nacimiento <= generaciones['generacion_x'].get("anio_final"):
        generacion = "X"
    elif anio_nacimiento >= generaciones['generacion_millenials'].get("anio_inicio") and \
        anio_nacimiento <= generaciones['generacion_millenials'].get("anio_final"):
        generacion = "Millenials"
    elif anio_nacimiento >= generaciones['generacion_z'].get("anio_inicio"):
        generacion = "Z"
    else:
        generacion = "Sin categoría para la generación"
    return generacion

    
def obtener_edad(persona_cumplio_anios):
    #Método para obtener la edad de una persona 
    if anio_nacimiento <= anio_actual and persona_cumplio_anios:
        edad = anio_actual - anio_nacimiento
    elif anio_nacimiento == anio_actual:
        edad = 0
    else:
        edad = anio_actual - anio_nacimiento -1
    return edad


def validar_datos():
    valido = False
    if isinstance(mes_nacimiento, int)  and isinstance(dia_nacimiento, int) \
        and isinstance(anio_nacimiento, int)  and mes_nacimiento in (meses) and \
            anio_nacimiento <= anio_actual:
        #Validar que el día sea correcto de acuerdo al año y mes de nacimiento
        ultimo_dia_mes = monthrange(anio_nacimiento, mes_nacimiento)[1] 
        if  dia_nacimiento >=1 and dia_nacimiento <= ultimo_dia_mes:
            valido = True  
    return valido


if validar_datos():
    cumplio_anios= False
    #Ya cumplio años en lo que va del año?
    if mes_nacimiento <= mes_actual and dia_nacimiento <= dia_actual:
        cumplio_anios = True

    #Resultados
    print("Cuantos años tiene? R:{}".format(obtener_edad(cumplio_anios)))
    if cumplio_anios == True:
        print("Ya cumplio años")
    else:
        print("No ha cumplido años")
    print("Genración: {}".format(obtener_generacion()))
else:
    print("Datos incorrectos")

