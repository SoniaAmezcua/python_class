#Archivos Json
import json
"""
json_file = 'archivo_json.json'
lista_contactos = []

#Lectura de Json
with open(json_file, 'r') as file:
    data = json.load(file) #data es diccionario
    for contacto in data['contactos']: #data['contactos'] es una lista y contacto es un diccionario
        lista_contactos.append(contacto)
        for key, value in contacto.items():
            print('{}:{}'.format(key, value))
    # print(type(data))
    # print(data)

#Escritura del Json
with open(json_file, 'w') as file2:
    new_contact ={
        "nombre": "Teresa",
        "telefono": "3126758900",
        "email": "Teresa@gmail.com"
    }
    lista_contactos.append(new_contact)
    new_data = {}
    new_data['contactos'] = lista_contactos
    json.dump(new_data, file2)
"""

json_file = 'agenda_json.json'
lista_contactos = []
opcion = int(input('''Ingrese una opcion (1 para guardar un contacto, 2 para visualizar agenda, 
3 para buscar un contacto, 4 para eliminar un contacto, 0 para salir)\n'''))

while opcion != 0:
    if opcion == 1:
        print('---- Agregar Contacto ----')
        nombre = input('Ingrese nombre del contacto\n')
        numero_telefonico = input('Ingrese numero de telefono del contacto\n')
        email = input('Ingrese email del contacto\n')
        with open(json_file, 'w') as file:
            new_contact = {
            "nombre": nombre,
            "telefono": numero_telefonico,
            "email": email
            }
            lista_contactos.append(new_contact)
            new_data = {}
            new_data['contactos'] = lista_contactos
            json.dump(new_data, file)               
    elif opcion == 2:
        print('---- Listar Agenda ----')
        with open(json_file, 'r') as file:
            data = json.load(file) #data es diccionario
            for contacto in data['contactos']: #data['contactos'] es una lista y contacto es un diccionario
                lista_contactos.append(contacto)
                for key, value in contacto.items():
                    print('{}:{}'.format(key, value))
    elif opcion == 3:
        print('---- Buscar Contacto ----')
        nombre = input('Ingrese nombre del contacto\n')
        with open(json_file, 'r') as file:
            data = json.load(file) #data es diccionario
            find = False
            for contacto in data['contactos']: #data['contactos'] es una lista y contacto es un diccionario
                if nombre in contacto.values():
                    print('---- Contacto ----')
                    for key, value in contacto.items():
                        print('{} : {}'.format(key,value))
                    find = True
            if not find:
                print('No existe un contacto con ese nombre')
    elif opcion == 4:
        nuevos_contactos = []
        print('---- Eliminar Contacto ----')
        nombre = input('Ingrese nombre del contacto\n')
        # Abrimos el archivo solo de lectura
        with open(json_file, 'r') as file:
            data = json.load(file) #data es diccionario
            find = False
            for contacto in data['contactos']: #data['contactos'] es una lista y contacto es un diccionario
                if nombre in contacto.values():
                    confirmar = int(input('Desea eliminar a {}? 1)Si 0) No'.format(nombre)))
                    if confirmar == 0:
                        nuevos_contactos.append(contacto)
                    find = True
                else:
                    nuevos_contactos.append(contacto)
        new_data = {}    
        new_data['contactos'] = nuevos_contactos
        # Abrimos el archivo en modo escritura
        with open(json_file, 'w') as file:
            json.dump(new_data,file)
        
        if not find:
            print('Contacto: {} no encontrado'.format(nombre))
    else:
        print('Opcion Invalida.\n')
    opcion = int(input('''Ingrese una opcion (1 para guardar un contacto, 2 para visualizar agenda,
    3 para buscar un contacto, 4 para eliminar un contacto, 0 para salir)\n'''))


