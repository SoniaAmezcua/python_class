from usuario import Usuario
from tarea import Tarea
import file_handler as fh


usuarios = []
tareas = []

def menu():
    print('---- Menu ----')
    print('1) Crear usuario\n')
    print('2) Exportar usuarios\n')
    print('3) Buscar usuario\n')
    print('4) Crear tarea\n')
    print('5) Mostrar tareas\n')
    print('6) Mostrar tarea por estado\n')
    print('7) Modificar estado de la tarea\n')
    print('8) Exportar tareas\n')
    print('9) Mostrar tareas por usuario\n')
    print('0) Salir\n')

def crear_usuario():
    print('---- Crear Usuario ----')
    nombre = input('Ingrese nombre del usuario\n')
    email = input('Ingrese email del usuario\n')
    usuarios.append(Usuario(nombre, email))

def export_data(data, tipo):
    opcion = int(input('Desea exportar {}? Presione 1 para confirmar o 0 para cancelar\n'.format(tipo)))
    if opcion==1:
        fh.exportar(data, tipo)

def buscar_usuario():
    print('---- Buscar Usuario ----')
    email = input('Ingrese email del usuario\n')
    for usuario in usuarios:
        if usuario.get_email() == email:
            return usuario    
    return None

def print_user_data(usuario):
    print('---- Usuario ----')
    print('Nombre: {}'.format(usuario.get_nombre()))
    print('Email : {}'.format(usuario.get_email()))

def crear_tarea():
    print('---- Crear Tarea ----')
    titulo = input('Ingrese titulo de la tarea\n')
    descripcion = input('Ingrese una descripcion de la tarea\n')
    prioridad = int(input('Ingrese una prioridad de la tarea(valores del 1 al 5 siendo 1 baja y 5 alta)\n'))
    usuario = None
    while usuario is None:
        usuario = buscar_usuario()
    tarea = Tarea(titulo, descripcion, prioridad, usuario.get_email())
    tareas.append(tarea)

def mostrar_listado_tareas():
    print('---- Mostrar tareas ----')
    for tarea in tareas:
        print('---- Tarea ----\n')
        print('Titulo: {}'.format(tarea.get_titulo()))
        print('Descripcion : {}'.format(tarea.get_descripcion()))
        print('Prioridad : {}'.format(tarea.get_prioridad()))
        print('Estado : {}'.format(tarea.get_estado()))
        print('Usuario asignado : {}'.format(tarea.get_usuario()))

def mostrar_tareas_estado(estado):
    print('---- Mostrar tareas ----')
    for tarea in tareas:
        if tarea.get_estado() == estado:
            print('---- Tarea ----\n')
            print('Titulo: {}'.format(tarea.get_titulo()))
            print('Descripcion : {}'.format(tarea.get_descripcion()))
            print('Prioridad : {}'.format(tarea.get_prioridad()))
            print('Estado : {}'.format(tarea.get_estado()))
            print('Usuario asignado : {}'.format(tarea.get_usuario()))

def mostrar_tareas_usuario():
    print('---- Tareas por usuario ----')
    usuario = input('Ingrese email del usuario\n')
    for tarea in tareas:
        if tarea.get_usuario() == usuario:
            print('---- Tarea ----\n')
            print('Titulo: {}'.format(tarea.get_titulo()))
            print('Descripcion : {}'.format(tarea.get_descripcion()))
            print('Prioridad : {}'.format(tarea.get_prioridad()))
            print('Estado : {}'.format(tarea.get_estado()))
            print('Usuario asignado : {}'.format(tarea.get_usuario()))
            
def buscar_tarea():
    print('---- Buscar tarea----')
    titulo = input('Ingrese titulo de la tarea\n')
    for tarea in tareas:
        if tarea.get_titulo() == titulo:
            return tarea    
    return None

def seleccionar_estado():
    estado = int(input('Ingrese el estado : 1 {}, 2 {}, 3 {}, 4 {} \n'.format(Tarea.BACKLOG, Tarea.TODO, Tarea.DOING, Tarea.RESOLVED)))
    while estado not in [1,2,3,4]:
        estado = int(input('Ingrese el estado : 1 {}, 2 {}, 3 {}, 4 {} \n'.format(Tarea.BACKLOG, Tarea.TODO, Tarea.DOING, Tarea.RESOLVED)))
    if estado == 1: 
        estado = Tarea.BACKLOG
    elif estado == 2: 
        estado = Tarea.TODO
    elif estado == 3: 
        estado = Tarea.DOING
    elif estado == 4: 
        estado = Tarea.RESOLVED 
    return estado

def modificar_estado_tarea():
    tarea = buscar_tarea()
    if tarea:
        print('Tarea {} con estado {}'.format(tarea.get_titulo(), tarea.get_estado()))
        estado = seleccionar_estado()
        tarea.set_estado(estado)
        print('Tarea {} con nuevo estado {}'.format(tarea.get_titulo(), tarea.get_estado()))
    else:
        print('No existe la tarea')  


menu()
opcion = int(input('''Ingrese una opcion)\n'''))
while opcion != 0:
    
    if opcion == 1:
        crear_usuario()

    elif opcion == 2:
        print('---- Exportar Usuarios----')
        export_data(usuarios,'usuarios')

    elif opcion == 3:
        usuario = buscar_usuario()
        if usuario:
            print_user_data(usuario)
        else:
            print('No existe un usuario con ese mail')
    elif opcion == 4:
        crear_tarea()

    elif opcion == 5:
        mostrar_listado_tareas()
    
    elif opcion == 6:
        print('---- Mostrar tareas por estado----')
        estado = seleccionar_estado()
        mostrar_tareas_estado(estado)

    elif opcion == 7:
        modificar_estado_tarea()

    elif opcion == 8:
        print('---- Exportar Tareas----')
        export_data(tareas,'tareas')

    elif opcion == 9:
        mostrar_tareas_usuario()

    menu()
    opcion = int(input('''Ingrese una opcion)\n'''))

# for tarea in tareas:
#     print(tarea.get_titulo())
#     print(tarea.get_descripcion())
#     print(tarea.get_estado())
#     print(tarea.get_prioridad())
#     print(tarea.get_usuario().get_nombre())
#     print(tarea.get_usuario().get_email()) 