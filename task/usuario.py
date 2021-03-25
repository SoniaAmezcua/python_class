class Usuario:

    def __init__(self,nombre, email) -> None:
        self.__nombre = nombre
        self.__email = email

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    

    