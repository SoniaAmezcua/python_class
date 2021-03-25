from motor import Motor

class Terrestre:

    __motor = Motor()
    __neumaticos = 0

    def _set_neumaticos(self, neumaticos):
        self.__neumaticos = neumaticos
    
    def get_neumaticos(self):
        return self.__neumaticos

    def get_nombre_motor(self):
        return self.__motor.get_nombre() #Encapsulamiento
