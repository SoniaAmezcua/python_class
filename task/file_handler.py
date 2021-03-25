import json

__usuarios_filename = 'usuarios.json'
__tareas_filename = 'tareas.json'

def exportar(data, tipo):
    if tipo == 'usuarios':
        dict_data = __usuarios_to_dict(data)
        __filename = __usuarios_filename 
    else:
        dict_data = __tareas_to_dict(data)
        __filename = __tareas_filename
    
    with open(__filename, 'w') as file:
        json.dump(dict_data, file)
        print('Información exportada en el archivo. {}'.format(__filename))

def __tareas_to_dict(tareas):
    dict_tareas = {}
    list_tareas = []
    for tarea in tareas:
        dict_tarea = {}
        dict_tarea['titulo'] = tarea.get_titulo()
        dict_tarea['descripcion'] = tarea.get_descripcion()
        dict_tarea['prioridad'] = tarea.get_prioridad()
        dict_tarea['estado'] = tarea.get_estado()
        dict_tarea['usuario'] = tarea.get_usuario()
        list_tareas.append(dict_tarea)
    dict_tareas['Tareas'] = list_tareas
    return dict_tareas

def __usuarios_to_dict(usuarios):
    dict_usuarios = {}
    list_usuarios = []
    for usuario in usuarios:
        dict_usuario = {}
        dict_usuario['nombre'] = usuario.get_nombre()
        dict_usuario['email'] = usuario.get_email()
        list_usuarios.append(dict_usuario)
    dict_usuarios['Usuarios'] = list_usuarios
    return dict_usuarios
