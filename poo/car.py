from terrestre import Terrestre

class Car(Terrestre):

    def __init__(self, marca, color):
        self.__marca = marca
        self.__color = color
        self._set_neumaticos(4)

    def __set_marca(self, marca):
        self.__marca = marca
    
    def get_marca(self):
        return self.__marca

    def __set_color(self, color):
        self.__color = color
    
    def get_color(self):
        return self.__color

    # def __get_combustible(self): #Metodo privado
    #     return self.__motor.get_combustible()
