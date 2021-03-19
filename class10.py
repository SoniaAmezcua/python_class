# import os
# separador = os.path.sep
# print(separador)

#Archivos
#Abrir archivo  Open()
# file = open('my_archivo.txt', 'a')
# file.write('Hola, Este es mi primer archivo\n')
# file.write('Modo a\n')
# file.close()

# file = open('my_archivo.txt', 'w')
# file.write('Modo w\n')
# file.write('Modo 1\n')
# file.write('Modo 2\n')
# file.write('Modo 3\n')
# file.close()

#Leer archivo  read() 
# file = open('my_archivo.txt', 'r')
#print(file.read())  # Leer todo el archivo
# print(file.readline()) # Leer linea por linea
# print(file.readline())
# print(file.readlines()) # Lista con los items 

# for  line in file.readlines():
#     print(line[:-1])
# file.close()


# agenda = {
#     'contactos' : []
# }

opcion = int(input('''Ingrese una opcion (1 para guardar un contacto, 2 para visualizar agenda, 
3 para buscar un contacto, 4 para eliminar un contacto, 0 para salir)\n'''))

while opcion != 0:
    if opcion == 1:
        print('---- Agregar Contacto ----')
        nombre = input('Ingrese nombre del contacto\n')
        numero_telefonico = input('Ingrese numero de telefono del contacto\n')
        email = input('Ingrese email del contacto\n')
        file = open('my_archivo.txt', 'a')
        file.write('{},{},{}\n'.format(nombre, numero_telefonico, email))
        file.close()               
    elif opcion == 2:
        print('---- Listar Agenda ----')
        file = open('my_archivo.txt', 'r')
        for  line in file.readlines():
            print(line[:-1])
        file.close() 
    elif opcion == 3:
        print('---- Buscar Contacto ----')
        nombre = input('Ingrese nombre del contacto\n')
        file = open('my_archivo.txt', 'r')
        find = False
        for  contacto in file.readlines():
            contacto_data = contacto.split(',')
            if nombre in contacto_data[0]:
                print('---- Contacto ----')
                print('Nombre: {}'.format(contacto_data[0]))
                print('Numero:{} Email:{}'.format(contacto_data[1]))
                print('Email:{}'.format(contacto_data[2]))
                find = True
        if not find:
            print('No existe un contacto con ese nombre')
        file.close() 
    elif opcion == 4:
        print('---- Eliminar Contacto ----')
        nombre = input('Ingrese nombre del contacto\n')
        # Abrimos el archivo solo de lectura
        file = open('my_archivo.txt', 'r')
        # Creamos una lista con cada una de sus lineas
        contactos_data = file.readlines()
        file.close()
        # Abrimos el archivo en modo sobreescritura
        file = open('my_archivo.txt', 'w')
        #Recorremos la lista
        for contacto in contactos_data:
            contacto_data = contacto.split(',') 
            if contacto_data[0] != nombre: #Si el contacto es diferente al contacto a eliminar lo escribimos en el archivo
                file.write(contacto)
        file.close()
    else:
        print('Opcion Invalida.\n')
    opcion = int(input('''Ingrese una opcion (1 para guardar un contacto, 2 para visualizar agenda,
    3 para buscar un contacto, 4 para eliminar un contacto, 0 para salir)\n'''))

